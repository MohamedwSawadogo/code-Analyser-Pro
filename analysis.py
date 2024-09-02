import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from fpdf import FPDF
import datetime

# Fonction pour importer les données à partir d'un fichier CSV
def import_data(file_path):
    return pd.read_csv(file_path)

# Fonction pour remplacer les valeurs négatives par zéro
def replace_negative_values_with_zero(data):
    numeric_cols = data.select_dtypes(include=[float, int]).columns
    data[numeric_cols] = data[numeric_cols].applymap(lambda x: max(x, 0))
    return data

# Fonction pour calculer les émissions totales pour chaque type de polluant
def calculate_total_emissions(data):
    pollutants = ['CO2_mass', 'CO_mass', 'NO_mass', 'NO2_mass', 'NOx_mass']
    total_emissions = {pollutant: data[pollutant].sum() for pollutant in pollutants}
    return total_emissions

# Fonction pour convertir les émissions totales en g/km
def convert_emissions_to_g_per_km(total_emissions, total_distance_km):
    emissions_g_per_km = {pollutant: total / total_distance_km for pollutant, total in total_emissions.items()}
    return emissions_g_per_km

# Fonction pour comparer les résultats avec les normes EURO 6
def compare_with_euro_6(emissions_g_per_km):
    euro_6_limits = {
        'CO_mass': 1.0,
        'NOx_mass': 0.06
    }
    results = {}
    for pollutant, value in emissions_g_per_km.items():
        if pollutant in euro_6_limits:
            results[pollutant] = {
                'value': value,
                'limit': euro_6_limits[pollutant],
                'compliant': value <= euro_6_limits[pollutant]
            }
    return results

# Fonction pour analyser les émissions
def analyze_emissions(file_path, total_distance_km):
    data = import_data(file_path)
    data = replace_negative_values_with_zero(data)
    total_emissions = calculate_total_emissions(data)
    emissions_g_per_km = convert_emissions_to_g_per_km(total_emissions, total_distance_km)
    results = compare_with_euro_6(emissions_g_per_km)
    return results

# Fonction pour générer des graphiques
def generate_graphs(file_path, x_axis, y_axes):
    data = import_data(file_path)
    data = replace_negative_values_with_zero(data)
    fig, ax = plt.subplots()

    axis_labels = {
        'Temps': 'secondes',
        'CO2_mass': 'g/s',
        'CO_mass': 'g/s',
        'NO_mass': 'g/s',
        'NO2_mass': 'g/s',
        'NOx_mass': 'g/s',
        'time' : 's',
        # Ajoutez d'autres colonnes et leurs unités ici si nécessaire
    }

    x_label = f"{x_axis} ({axis_labels.get(x_axis, '')})"
    y_label = ', '.join([f"{y} ({axis_labels.get(y, '')})" for y in y_axes])

    for y_axis in y_axes:
        ax.plot(data[x_axis], data[y_axis], label=y_axis)

        # Colorier les zones de conformité et de non-conformité
        if y_axis in ['CO_mass', 'NOx_mass']:
            limit = 1.0 if y_axis == 'CO_mass' else 0.06
            ax.fill_between(data[x_axis], data[y_axis], limit, where=(data[y_axis] <= limit), facecolor='green', alpha=0.3, interpolate=True, label='Conforme')
            ax.fill_between(data[x_axis], data[y_axis], limit, where=(data[y_axis] > limit), facecolor='red', alpha=0.3, interpolate=True, label='Non Conforme')
            ax.axhline(y=limit, color='blue', linestyle='--', label=f'Limite {y_axis}')

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(f'Visualisation des Données : {", ".join(y_axes)} en fonction de {x_axis}', fontweight='bold')
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())
    canvas = FigureCanvas(fig)
    return canvas

# Fonction pour calculer les écarts, générer des commentaires et des corrections
def calculate_anomalies_and_generate_report(data, x_axis, y_axes):
    euro_6_limits = {
        'CO_mass': 1.0,
        'NOx_mass': 0.06
    }
    anomalies = []

    for y_axis in y_axes:
        if y_axis in euro_6_limits:
            limit = euro_6_limits[y_axis]
            for idx, row in data.iterrows():
                if row[y_axis] > limit:
                    ecart = row[y_axis] - limit
                    ecart_percent = (ecart / limit) * 100
                    comment = f"La valeur de {y_axis} ({row[y_axis]}) dépasse la limite supérieure ({limit}) par {ecart:.2f} ({ecart_percent:.2f}%)."
                    correction = generate_correction(y_axis, ecart_percent)
                    anomalies.append({
                        'Temps': row[x_axis],
                        'Polluant': y_axis,
                        'Valeur': row[y_axis],
                        'Écart (%)': ecart_percent,
                        'Commentaire': comment,
                        'Correction': correction
                    })
    return anomalies

# Fonction pour générer des corrections basées sur le polluant et l'écart
def generate_correction(pollutant, ecart_percent):
    corrections = {
        'CO_mass': [
            "Vérifiez le système d'injection de carburant.",
            "Assurez-vous qu'il n'y a pas de problèmes d'allumage.",
            "Contrôlez l'état du catalyseur."
        ],
        'NOx_mass': [
            "Vérifiez le système de réduction catalytique sélective (SCR).",
            "Ajustez le rapport air/carburant.",
            "Contrôlez l'état du convertisseur catalytique."
        ]
    }
    correction_messages = corrections.get(pollutant, [])
    if ecart_percent > 50:
        return correction_messages[0]
    elif 20 < ecart_percent <= 50:
        return correction_messages[1]
    else:
        return correction_messages[2] if len(correction_messages) > 2 else ""

# Fonction pour exporter les données en PDF
def export_to_pdf(data, file_path, title):
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.ln(20)  # Ajouter un espace après le logo

    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, txt=f"{title} - {date_time}", ln=True, align='C')

    pdf.set_font("Arial", size=10)

    col_widths = [20, 20, 20, 30, 120, 120]
    row_height = pdf.font_size * 1.5

    # En-têtes du tableau
    headers = ["Temps", "Polluant", "Valeur", "Écart (%)", "Commentaire", "Correction"]
    for idx, header in enumerate(headers):
        pdf.cell(col_widths[idx], row_height, txt=header, border=1, align='C')
    pdf.ln(row_height)

    # Données du tableau
    for row in data:
        for idx, item in enumerate(row):
            pdf.cell(col_widths[idx], row_height, txt=str(item), border=1)
        pdf.ln(row_height)
    
    pdf.output(file_path)
    print(f"Data exported to PDF successfully at {file_path}!")
