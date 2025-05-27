# services/reporting_service/app.py

class ReportGenerator:
    def __init__(self, service_name: str):
        self.service_name = service_name
        print(f"ReportGenerator initialized for {self.service_name}")

    def generate_summary_report(self, data: list[int]) -> dict:
        """Generates a summary report from a list of numerical data."""
        if not data:
            return {"status": "success", "summary": "No data to process."}

        total = sum(data)
        average = total / len(data)
        
        return {
            "status": "success",
            "service": self.service_name,
            "total_items": len(data),
            "sum": total,
            "average": round(average, 2)
        }

    def generate_detailed_report(self, data: list[dict]) -> list[dict]:
        """Generates a detailed report, adding a status to each item."""
        if not data:
            return []
        
        detailed_report = []
        for i, item in enumerate(data):
            item_copy = item.copy()
            item_copy['report_status'] = 'processed'
            item_copy['report_id'] = f"REPORT-{i+1}"
            detailed_report.append(item_copy)
        return detailed_report