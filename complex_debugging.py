import logging
import concurrent.futures

# Configure the logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def deep_nested_operation(value):
    """
    Perform a deep nested operation on the provided value.

    Args:
        value (int): The value to be processed.

    Returns:
        int: The result of the deep nested operation.

    Raises:
        ValueError: If the provided value is negative.
    """
    logging.debug(f"Performing deep nested operation on {value}")
    if value < 0:
        raise ValueError("Value must be non-negative.")
    return value * 3

def complex_operation(data):
    """
    Perform a complex operation on the provided data.

    Args:
        data (dict): The data dictionary containing a 'value' key.

    Returns:
        int: The final result of the complex operation.

    Raises:
        TypeError: If the input data is not a dictionary.
        KeyError: If the 'value' key is missing in the data.
        ValueError: If the value is negative in deep_nested_operation.
    """
    logging.debug(f"Performing complex operation on {data}")
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary.")
    if 'value' not in data:
        raise KeyError("'value' key is missing in the data.")
    
    intermediate_result = data['value'] * 2
    logging.debug(f"Intermediate result: {intermediate_result}")
    
    final_result = deep_nested_operation(intermediate_result)
    logging.debug(f"Final result: {final_result}")
    
    return final_result

def process_nested_data(data_list):
    """
    Process a list of data dictionaries sequentially, handling exceptions.

    Args:
        data_list (list): A list of dictionaries to be processed.

    Returns:
        list: A list of results from the complex_operation function.
    """
    results = []
    for data in data_list:
        try:
            result = complex_operation(data)
            results.append(result)
        except (TypeError, KeyError, ValueError) as e:
            logging.error(f"Error processing data: {e}")
    return results

def process_data_concurrently(data_list):
    """
    Process a list of data dictionaries concurrently using threads.

    Args:
        data_list (list): A list of dictionaries to be processed.

    Returns:
        list: A list of results from the complex_operation function processed concurrently.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_data = {executor.submit(complex_operation, data): data for data in data_list}
        results = []
        for future in concurrent.futures.as_completed(future_to_data):
            data = future_to_data[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                logging.error(f"Error processing data {data}: {e}")
    return results

# Sample data
data_list = [{'id': 1, 'value': 10}, {'id': 2}, {'id': 3, 'value': -5}, {'id': 4, 'value': 20}, 'invalid data']

logging.info("Starting the main script")

# Sequential processing
sequential_results = process_nested_data(data_list)
logging.info(f"Sequential processing results: {sequential_results}")

# Concurrent processing
concurrent_results = process_data_concurrently(data_list)
logging.info(f"Concurrent processing results: {concurrent_results}")

logging.info("Main script finished")
