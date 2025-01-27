# config.py
KI_MODEL = "process-mining-ai"

DEFAULT_OPTIONS = {
    "goal": ["Fehlererkennung", "Performance-Optimierung", "Compliance", "Prozessverständnis", "Ressourcenoptimierung", "Prognose", "Ich weiß nicht"],
    "num_traces": ["Weniger als 100", "100–1000", "Mehr als 1000", "Ich weiß nicht"],
    "num_activities": ["Weniger als 10", "10–50", "Mehr als 50", "Ich weiß nicht"],
    "process_complexity": ["Einfach", "Mittel", "Hoch", "Ich weiß nicht"],
    "has_loops": ["Ja", "Nein", "Ich weiß nicht"],
    "has_parallelism": ["Ja", "Nein", "Ich weiß nicht"],
    "data_completeness": ["Ja", "Nein", "Teilweise", "Ich weiß nicht"],
    "data_noise": ["Ja", "Nein", "Ich weiß nicht"],
    "has_timestamps": ["Ja", "Nein", "Ich weiß nicht"],
    "easy_interpretation": ["Ja", "Nein", "Ich weiß nicht"],
    "speed_importance": ["Ja", "Nein", "Ich weiß nicht"],
    "programming_language": ["Python", "Java", "Andere", "Keine Präferenz"]
}