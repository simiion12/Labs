from typing import Dict, Any
from datetime import datetime
from ..interfaces.weather_observer import WeatherObserver

class AlertSystem(WeatherObserver):
    def update(self, weather_data: Dict[str, Any]) -> None:
        self._check_temperature(weather_data)
        self._check_wind(weather_data)
        self._check_precipitation(weather_data)

    def _check_temperature(self, data: Dict[str, Any]) -> None:
        temp = data.get('temperature_c')
        if temp > 5:
            self._log_alert(f"🔥 EXTREME HEAT WARNING: {temp}°C in {data['location']}")
        elif temp > -10:
            self._log_alert(f"❄️ EXTREME COLD WARNING: {temp}°C in {data['location']}")

    def _check_wind(self, data: Dict[str, Any]) -> None:
        wind = data.get('wind_mph', 0)
        if wind > 50:
            self._log_alert(f"💨 HIGH WIND ADVISORY: {wind} mph in {data['location']}")

    def _check_precipitation(self, data: Dict[str, Any]) -> None:
        precip = data.get('precipitation_mm', 0)
        if precip > 50:
            self._log_alert(f"🌧️ HEAVY RAIN ALERT: {precip}mm in {data['location']}")

    def _log_alert(self, message: str) -> None:
        print(f"\n[ALERT] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(message)
