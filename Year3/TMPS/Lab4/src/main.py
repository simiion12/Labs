from Year3.TMPS.Lab4.src.facade.weather_facade import WeatherSystemFacade

def main():
    weather_system = WeatherSystemFacade()

    while True:
        print("\nWeather Information System")
        print("1. Get Single Station Report")
        print("2. Get Regional Report")
        print("3. Manage Regions")
        print("4. Manage Alert System")
        print("5. Manage Statistic Calculation Methods")
        print("6. View Cache Statistics")
        print("7. Exit")

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
            print("3. List all regions")
            while True:
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
                elif mgmt_choice == '3':
                    regions = weather_system.regions.keys()
                    if regions:
                        print("\nAvailable regions:")
                        for region in regions:
                            print(f"- {region}")
                    else:
                        print("No regions available")
                else:
                    break

        elif choice == '4':
            weather_system.manage_alerts()

        elif choice == '5':
            weather_system.manage_calculation_methods()

        elif choice == '6':
            stats = weather_system.cache.get_stats()
            print("\nCache Statistics:")
            print(f"Size: {stats['size']}/{stats['max_size']}")
            print(f"TTL: {stats['ttl_minutes']} minutes")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()