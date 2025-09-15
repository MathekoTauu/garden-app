def get_season_advice(season):
    """Return gardening advice based on the season."""
    advice = ""
    if season.lower() == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season.lower() == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"
    return advice

def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    advice = ""
    if plant_type.lower() == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type.lower() == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    return advice

def recommend_plants(season):
    """Recommend plants based on the season."""
    recommendations = {
        "summer": ["Sunflower", "Marigold"],
        "winter": ["Pansies", "Hellebores"]
    }
    return recommendations.get(season.lower(), [])

# Get user input for season and plant type
season = input("Enter the season (summer/winter): ")  # User input for season
plant_type = input("Enter the plant type (flower/vegetable): ")  # User input for plant type

# Gather advice
advice = get_season_advice(season) + get_plant_advice(plant_type)

# Print the generated advice
print(advice)

# Recommend plants for the entered season
recommended_plants = recommend_plants(season)
if recommended_plants:
    print(f"Recommended plants for {season}: {', '.join(recommended_plants)}")
