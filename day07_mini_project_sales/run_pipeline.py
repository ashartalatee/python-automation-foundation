from input_module import get_sales_data
from processing_module import clean_sales_data
from analysis_module import analyze_sales
from output_module import print_report

def main():
    raw_data = get_sales_data()
    cleaned_data = clean_sales_data(raw_data)
    result = analyze_sales(cleaned_data)
    print_report(result)

if __name__ == "__main__":
    main()