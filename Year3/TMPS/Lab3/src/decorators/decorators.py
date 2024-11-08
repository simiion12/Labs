class AlertDecorator:
    def __init__(self, weather_report):
        self._weather_report = weather_report

    def get_data(self):
        alerts = self._generate_weather_alerts(self._weather_report)
        return self._combine_report_and_alerts(self._weather_report, alerts)

    def _generate_weather_alerts(self, data):
        alerts = []
        if data.temperature_c > 35:
            alerts.append("Extreme heat warning!")
        if data.wind_mph > 50:
            alerts.append("High wind advisory!")
        return alerts

    def _combine_report_and_alerts(self, weather_report, alerts):
        alerts_str = "\n".join(alerts) if alerts else "No active weather alerts."
        return f"""
{alerts_str}

{weather_report}
"""