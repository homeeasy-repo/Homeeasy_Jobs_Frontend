import psycopg2
import csv

# Database connection parameters
db_params = {
    'dbname': 'd5pt3225ki095v',
    'user': 'readonly',
    'password': 'p2e0dfd8702aac2f2b98b80f2e14430fb7d3cec6f8aec1770701283042b112712',
    'host': 'ec2-23-20-93-193.compute-1.amazonaws.com',
    'port': '5432'
}

# SQL query
query = """
    SELECT
    i.id,
    i.indeed_id,
    i.fname AS first_name,
    i.emailed_on::date AS "Date",
    CASE 
        WHEN i.activity_submitted IS NOT NULL THEN 'Completed' 
        ELSE 'Not Completed' 
    END AS submission_status,
    i.activity_submitted AS "Activity Submitted Timestamp",
    i.emailed_interview AS "Interviewed Timestamp",
    i.hired AS "Hired Timestamp"
FROM 
    indeedcandidate i
WHERE 
    i.emailed_on IS NOT NULL
ORDER BY 
    i.emailed_on::date DESC;
"""

try:
    # Establishing the connection
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Executing the query
    cursor.execute(query)
    records = cursor.fetchall()

    # CSV file path and headers
    csv_file = 'raw_data_statistics.csv'
    csv_headers = ['Date', 'Emailed', 'Activity Submitted', 'Interviewed', 'Hired']

    # Writing to CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(csv_headers)
        # Write rows from database records
        writer.writerows(records)

    print(f"Data successfully written to {csv_file}")

    # Closing the cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error: {e}")
