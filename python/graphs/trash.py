def calculate_avg_height(heights):
    sum = 0
    for height in heights:
        sum += int(height)
    avg = sum / len(heights)
    return avg


student_heights = input("Enter the heights: ").split()
average = calculate_avg_height(student_heights)
print(average)
