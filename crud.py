from connection import *
from schemas import *

def get_all_reports():
    connection = get_db_connection()
    reports = []
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reports ORDER BY date ASC")
        reports = cursor.fetchall()
    except Error as e:
        print(f"ERROR: {e}")
    finally:
        close_db_connection(connection)
    return reports

def get_report(id: int):
    connection = get_db_connection()

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reports WHERE id = %s", (id,))
        report = cursor.fetchone()
        return report
    except Error as e:
        print(f"Error to get report : {e}")
    finally:
        close_db_connection(connection)

def create_report(report : ReportCreate):
    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO reports (client, num_receipt, date, description, amount) VALUES (%s, %s, %s, %s, %s)",
                       (report.client, report.num_receipt, report.date, report.description, report.amount))
        connection.commit()
        return report
    except Error as e:
        print(f"Error to create report : {e}")
    finally:
        close_db_connection(connection)

def update_report(id: int, report: ReportCreate):
    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE reports 
            SET client = %s, num_receipt = %s, date = %s, description = %s, amount = %s
            WHERE id = %s
        """, (report.client, report.num_receipt, report.date, report.description, report.amount, id))
        connection.commit()
        return report
    except Error as e:
        print(f"Error to update report : {e}")
    finally:
        close_db_connection(connection)

def get_report_month_year(month: str, year: str):
    connection = get_db_connection()

    try:
        if month and not year:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reports WHERE MONTH(date) = %s ORDER BY date ASC", (month,))
            reports = cursor.fetchall()
            return reports
        
        elif not month and year:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reports WHERE YEAR(date) = %s ORDER BY date ASC", (year,))
            reports = cursor.fetchall()
            return reports
        
        elif month and year:
            if month == '00':
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM reports WHERE YEAR(date) = %s ORDER BY date ASC", (year, ))
                reports = cursor.fetchall()
                return reports
            else:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM reports WHERE MONTH(date) = %s AND YEAR(date) = %s ORDER BY date ASC", (month, year))
                reports = cursor.fetchall()
                return reports

        else:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reports ORDER BY date ASC")
            reports = cursor.fetchall()
            return reports

    except Error as e:
        print(f"Error to get reports for month and year: {e}")
    finally:
        close_db_connection(connection)


def delete_report(id: int):
    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM reports WHERE id = %s", (id, ))
        connection.commit()
        return "Eliminado correctamente"
    except Error as e:
        print(f"Error to delete report : {e}")
    finally:
        close_db_connection(connection)