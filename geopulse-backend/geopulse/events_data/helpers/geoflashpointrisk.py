from geopulse.events_data.models import GeoFlashpointRisk
import common.model_helper as model_helper
def get_nonexistent_event_ids(event_ids:list) -> list:
    """
    Given a list of event IDs, return the IDs that are not already in the GeoFlashpointRisk table.
    
    Parameters:
        - event_ids: list of int, list of event IDs to check
    
    Returns:
        - list of int, event IDs that do not exist in the table
    """
    # Query the database to get existing EVENT_IDs that are in the provided list
    existing_ids = GeoFlashpointRisk.objects.filter(EVENT_ID__in=event_ids).values_list('EVENT_ID', flat=True)
    
    # Convert the QuerySet to a set for faster lookup
    existing_ids_set = set(existing_ids)
    
    # Filter out the existing IDs from the initial list
    nonexistent_ids = [event_id for event_id in event_ids if event_id not in existing_ids_set]
    
    return nonexistent_ids

def get_geoflashpointrisk_fields():
    return model_helper.get_model_fields(GeoFlashpointRisk)
