from Year3.TMPS.Lab3.src.facade.weather_facade import WeatherSystemFacade


def main():
    weather_system = WeatherSystemFacade()

    while True:
        print("\nWeather Information System")
        print("1. Get Single Station Report")
        print("2. Get Regional Report")
        print("3. Manage Regions")
        print("4. View Cache Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            location = input("Enter location: ")
            date = input("Enter date (yyyy-mm-dd): ")

            report = weather_system.get_weather_report(location, date)
            print(report)

        elif choice == '2':
            region = input("Enter region name: ")
            date = input("Enter date (yyyy-mm-dd): ")

            report = weather_system.get_region_report(region, date)
            print(report)

        elif choice == '3':
            print("\nRegion Management")
            print("1. Create new region")
            print("2. Add station to region")

            mgmt_choice = input("Enter choice: ")
            if mgmt_choice == '1':
                region = input("Enter new region name: ")
                weather_system.add_region(region)
                print(f"Region {region} created")
            elif mgmt_choice == '2':
                region = input("Enter region name: ")
                station = input("Enter station location: ")
                weather_system.add_station_to_region(region, station)
                print(f"Added {station} to {region}")

        elif choice == '4':
            stats = weather_system.cache.get_stats()
            print("\nCache Statistics:")
            print(f"Size: {stats['size']}/{stats['max_size']}")
            print(f"TTL: {stats['ttl_minutes']} minutes")

        elif choice == '5':
            print("Exiting...")
            break


if __name__ == '__main__':
    main()