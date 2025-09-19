import csv
import os

def read_student_data(csv_filename):
    """
    Read student data from CSV file.
    
    Args:
        csv_filename (str): Name of the CSV file to read
        
    Returns:
        list: List of dictionaries containing student data
    """
    students = []
    
    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Validate required columns
            required_columns = ['Name', 'Math', 'Science', 'English']
            if not all(col in csv_reader.fieldnames for col in required_columns):
                raise ValueError("CSV must contain columns: Name, Math, Science, English")
            
            for row in csv_reader:
                # Convert marks to integers and validate
                try:
                    student = {
                        'Name': row['Name'].strip(),
                        'Math': int(row['Math']),
                        'Science': int(row['Science']),
                        'English': int(row['English'])
                    }
                    
                    # Validate marks are between 0 and 100
                    if not all(0 <= mark <= 100 for mark in [student['Math'], student['Science'], student['English']]):
                        print(f"Warning: Marks for {student['Name']} should be between 0 and 100")
                        continue
                        
                    students.append(student)
                    
                except ValueError as e:
                    print(f"Warning: Invalid marks for {row['Name']}: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return students

def calculate_student_stats(students):
    """
    Calculate total and average marks for each student.
    
    Args:
        students (list): List of student dictionaries
        
    Returns:
        list: List of student dictionaries with calculated stats
    """
    for student in students:
        total = student['Math'] + student['Science'] + student['English']
        average = round(total / 3, 2)
        
        student['Total'] = total
        student['Average'] = average
    
    return students

def display_results(students):
    """
    Display student results in a formatted table.
    
    Args:
        students (list): List of student dictionaries with calculated stats
    """
    if not students:
        print("No student data to display.")
        return
    
    # Find the longest name for proper column width
    max_name_length = max(len(student['Name']) for student in students)
    name_width = max(max_name_length, 4)  # Minimum width of 4 for "Name"
    
    # Print header
    print(f"{'Name':<{name_width}}  {'Total':<6}  {'Average':<8}")
    print("-" * (name_width + 6 + 8 + 4))  # +4 for spacing
    
    # Print student data
    for student in students:
        print(f"{student['Name']:<{name_width}}  {student['Total']:<6}  {student['Average']:<8.2f}")

def create_sample_csv():
    """
    Create a sample CSV file if it doesn't exist.
    """
    sample_data = [
        ['Name', 'Math', 'Science', 'English'],
        ['Alice', '85', '90', '78'],
        ['Bob', '70', '88', '92'],
        ['Charlie', '95', '87', '89'],
        ['Diana', '78', '92', '85'],
        ['Eve', '88', '76', '94']
    ]
    
    try:
        with open('students.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(sample_data)
        print("Sample students.csv file created successfully!")
    except Exception as e:
        print(f"Error creating sample file: {e}")

def main():
    """
    Main function to run the student marks analyzer.
    """
    csv_filename = 'students.csv'
    
    # Check if CSV file exists, create sample if it doesn't
    if not os.path.exists(csv_filename):
        print(f"File '{csv_filename}' not found. Creating sample file...")
        create_sample_csv()
        print()
    
    # Read student data
    print("Reading student data...")
    students = read_student_data(csv_filename)
    
    if not students:
        print("No valid student data found. Please check your CSV file.")
        return
    
    # Calculate statistics
    print("Calculating student statistics...")
    students_with_stats = calculate_student_stats(students)
    
    # Display results
    print("\nStudent Results:")
    print("=" * 50)
    display_results(students_with_stats)
    
    # Display summary statistics
    print("\n" + "=" * 50)
    print("Summary Statistics:")
    
    if students_with_stats:
        total_students = len(students_with_stats)
        class_math_avg = sum(s['Math'] for s in students_with_stats) / total_students
        class_science_avg = sum(s['Science'] for s in students_with_stats) / total_students
        class_english_avg = sum(s['English'] for s in students_with_stats) / total_students
        class_overall_avg = sum(s['Average'] for s in students_with_stats) / total_students
        
        print(f"Total Students: {total_students}")
        print(f"Class Average - Math: {class_math_avg:.2f}")
        print(f"Class Average - Science: {class_science_avg:.2f}")
        print(f"Class Average - English: {class_english_avg:.2f}")
        print(f"Class Overall Average: {class_overall_avg:.2f}")
        
        # Find top performer
        top_student = max(students_with_stats, key=lambda x: x['Average'])
        print(f"\nTop Performer: {top_student['Name']} (Average: {top_student['Average']:.2f})")

if __name__ == "__main__":
    main()
