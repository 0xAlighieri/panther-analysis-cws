from panther_ipinfo_helpers import IPInfoLocation


def rule(event):
    return True


def title(event):
    custom_lookup_name = "my_cool_lookup"
    custom_lookup_data = event.lookup(
        custom_lookup_name, event.get("ClientRequestHost")
    )
    name = custom_lookup_data.get("name")
    job = custom_lookup_data.get("job")

    return f" {name} - {job}"


def alert_context(event):
    global ip_info_location
    ip_info_location = IPInfoLocation(event)
    match_field = "clientIP"

    city = ip_info_location.city(match_field)
    region = ip_info_location.region(match_field)
    country = ip_info_location.country(match_field)

    return {"city": city, "region": region, "country": country}
