import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

try:
    marks = int(input("Enter marks: "))
    logging.info("Marks entered successfully")
except ValueError:
    logging.error("Invalid marks entered")
    print("Please enter numeric marks only.")