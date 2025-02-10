# Summary Item List from Episodes 2-5:

# 2. Numeric Types
# 3. Sequence Types
# 4. Strings
# 5. Dictionary

"""Extra Problem: Stretch Goal"""
# It's a stetch because we haven't gone over loops or functions yet.  But, if you're feeling ambitious, give it a try.

full_names = "John Doe, Jane Smith, Jack Dane, Jane Jackson"
streets_by_lastname = {'Doe': '123 Elm St', 'Smith': '456 Oak St', 'Dane': '789 Pine St', 'Jackson': '1011 Cedar St'}
zipcodes_by_lastname = (('Doe', '12345'), ('Smith', '23456'), ('Dane', '34567'), ('Jackson', '45678'))
city_and_state_by_zipcode = {'12345': ['Springfield', 'IL'], '23456': ['Rivertown', 'MI'], '34567': ['Hill Valley', 'CA'], '45678': ['Smallville', 'KS']}
def main():
    """
    Goal, create a multiline string that looks like this:
    Full Name
    Street Address
    City, State Zipcode
    """

    # 1. Separate out the last names from the full names and place them in a list.
    # 2. Loop through the list of last names and use them to get the street address from the streets_by_lastname dictionary.
    # 3. Use the last names to gain access to the zipcodes in the zipcodes_by_lastname tuple.
    # 4. Use the zipcodes to get the city and state from the city_and_state_by_zipcode dictionary.
    # 5. Create a dictionary with the full name as the key and the multiline string as the value.




    pass

if __name__ == "__main__":
    main()