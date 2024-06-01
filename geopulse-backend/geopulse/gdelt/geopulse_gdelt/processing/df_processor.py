import pandas as pd
import geopulse.events_data.helpers.geoflashpointrisk as gfpr_helper

def filter_dataframe(csv_df, actor_codes, cameo_codes):
    """
    Filter the DataFrame to only include rows where 'INITIATOR_TYPE1_CODE' or 'TARGET_TYPE_CODE' (or their secondary and tertiary codes)
    is in the actors list and 'EVENT_CODE' is in the cameos list.

    Parameters:
        - csv_df: Pandas DataFrame to filter
        - actor_codes: list of str, actor codes to filter on
        - cameo_codes: list of str, cameo codes to filter on

    Returns:
        - filtered_df: Filtered Pandas DataFrame
    """
    initiator_codes_columns = ['INITIATOR_CODE', 'INITIATOR_TYPE1_CODE', 'INITIATOR_TYPE2_CODE', 'INITIATOR_TYPE3_CODE']
    target_codes_columns = ['TARGET_CODE', 'TARGET_TYPE1_CODE', 'TARGET_TYPE2_CODE', 'TARGET_TYPE3_CODE']
    
    # Create masks for initiator and target codes
    initiator_mask = csv_df[initiator_codes_columns].isin(actor_codes).any(axis=1)
    target_mask = csv_df[target_codes_columns].isin(actor_codes).any(axis=1)
    
    # Create a mask for the condition where EVENT_CODE is in the cameo codes list
    cameo_mask = csv_df['EVENT_CODE'].isin(cameo_codes)
    
    # Combine the masks to filter the DataFrame
    filtered_df = csv_df[(initiator_mask | target_mask) & cameo_mask]
    
    return filtered_df

def preprocess_dataframe(csv_df):
    """
    Preprocess the DataFrame to ensure unique data, convert to strings, and format date columns.

    Parameters:
        - csv_df: Pandas DataFrame to preprocess

    Returns:
        - preprocessed_df: Preprocessed Pandas DataFrame
    """
    # Ensure unique data by filtering out existing EVENT_IDs
    csv_df_event_ids = csv_df['EVENT_ID'].tolist()
    nonexistent_ids = gfpr_helper.get_nonexistent_event_ids(csv_df_event_ids)
    csv_df = csv_df[csv_df['EVENT_ID'].isin(nonexistent_ids)]
    
    # Convert all columns to strings
    csv_df = csv_df.astype(str)
    
    # Format the DATEADDED column
    csv_df['DATEADDED'] = pd.to_datetime(csv_df['DATEADDED'], format='%Y%m%d%H%M%S', errors='coerce')
    
    return csv_df

def process_df():
    """
    Main function to load, preprocess, and filter the DataFrame.
    """
    
    # Load configuration values
    actor_codes, cameo_codes = load_configuration()
    
    # Load the DataFrame from the CSV module
    csv_df = csv_to_dataframe()  # Assuming csv_to_dataframe already handles the file path and returns a DataFrame
    
    # Preprocess the DataFrame
    preprocessed_df = preprocess_dataframe(csv_df)
    
    # Filter the DataFrame
    filtered_df = filter_dataframe(preprocessed_df, actor_codes, cameo_codes)
    
    # Print the filtered DataFrame to verify
    print(filtered_df.head())

# Example usage
if __name__ == "__main__":
    main()

