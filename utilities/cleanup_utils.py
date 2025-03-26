import os
import re
import glob
import shutil
from datetime import datetime
from config.config import REPORTS_DIR, SCREENSHOTS_DIR

def get_file_timestamp(filename):
    """
    Extract timestamp from a filename
    
    Args:
        filename: Name of the file
    
    Returns:
        datetime object representing the timestamp in the filename
    """
    # Extract timestamp in format YYYY-MM-DD_HH-MM-SS
    match = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', filename)
    if match:
        timestamp_str = match.group(1)
        try:
            return datetime.strptime(timestamp_str, '%Y-%m-%d_%H-%M-%S')
        except ValueError:
            # If conversion fails, return a very old date
            return datetime.min
    return datetime.min

def cleanup_reports(max_reports=5):
    """
    Keep only the specified number of most recent reports
    
    Args:
        max_reports: Maximum number of reports to keep
    """
    if not os.path.exists(REPORTS_DIR):
        return
        
    # Get all HTML report files
    report_files = glob.glob(os.path.join(REPORTS_DIR, "test_report_*.html"))
    
    # Sort by timestamp (newest first)
    report_files.sort(key=get_file_timestamp, reverse=True)
    
    # Keep only the latest N reports
    files_to_delete = report_files[max_reports:]
    
    # Delete older files
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted old report: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error deleting report {file_path}: {e}")

def cleanup_screenshots(option="match_reports", max_screenshots=None, reports_to_match=5):
    """
    Manage screenshots based on selected strategy
    
    Args:
        option: "last_execution" to keep only latest screenshots, 
                "match_reports" to organize screenshots to match reports
        max_screenshots: Maximum number of screenshots to keep (only used with last_execution option)
        reports_to_match: Number of latest reports to match screenshots with (only used with match_reports option)
    """
    if not os.path.exists(SCREENSHOTS_DIR):
        return
    
    # Check for important folder and delete it if it exists
    important_folder = os.path.join(SCREENSHOTS_DIR, "important")
    if os.path.exists(important_folder) and os.path.isdir(important_folder):
        try:
            shutil.rmtree(important_folder)
            print(f"Removed 'important' folder as requested")
        except Exception as e:
            print(f"Error removing 'important' folder: {e}")
           
    # Get all screenshot files (only in the root screenshots directory)
    screenshot_files = glob.glob(os.path.join(SCREENSHOTS_DIR, "*.png"))
    
    # If no unorganized screenshots in the root directory, we can proceed to cleanup existing folders
    if len(screenshot_files) == 0 and option == "match_reports":
        # Get all report files
        report_files = glob.glob(os.path.join(REPORTS_DIR, "test_report_*.html"))
        
        # Sort by timestamp (newest first)
        report_files.sort(key=get_file_timestamp, reverse=True)
        
        # Keep only the latest N reports
        recent_reports = report_files[:reports_to_match]
        
        # Extract timestamps from reports
        report_timestamps = [get_file_timestamp(r) for r in recent_reports]
        valid_folder_names = [t.strftime('%Y-%m-%d_%H-%M-%S') for t in report_timestamps]
        
        # Remove any folders that don't match recent report timestamps
        timestamp_folders = [d for d in os.listdir(SCREENSHOTS_DIR) 
                           if os.path.isdir(os.path.join(SCREENSHOTS_DIR, d))]
        
        for folder in timestamp_folders:
            if folder not in valid_folder_names:
                folder_path = os.path.join(SCREENSHOTS_DIR, folder)
                try:
                    shutil.rmtree(folder_path)
                    print(f"Removed old screenshot folder: {folder}")
                except Exception as e:
                    print(f"Error removing folder {folder_path}: {e}")
        
        return
    
    # Handle screenshots based on the selected option
    if option == "last_execution":
        # Sort by timestamp (newest first)
        screenshot_files.sort(key=get_file_timestamp, reverse=True)
        
        # If max_screenshots is None, find the newest timestamp and keep only files with that timestamp
        if max_screenshots is None:
            if not screenshot_files:
                return
                
            newest_timestamp = get_file_timestamp(screenshot_files[0])
            files_to_keep = [f for f in screenshot_files if get_file_timestamp(f).date() == newest_timestamp.date()]
            files_to_delete = [f for f in screenshot_files if f not in files_to_keep]
        else:
            # Keep only the latest N screenshots
            files_to_delete = screenshot_files[max_screenshots:]
        
        # Delete older files
        for file_path in files_to_delete:
            try:
                os.remove(file_path)
                print(f"Deleted old screenshot: {os.path.basename(file_path)}")
            except Exception as e:
                print(f"Error deleting screenshot {file_path}: {e}")
                
    elif option == "match_reports":
        # Get all report files
        report_files = glob.glob(os.path.join(REPORTS_DIR, "test_report_*.html"))
        
        # Sort by timestamp (newest first)
        report_files.sort(key=get_file_timestamp, reverse=True)
        
        # Keep only the latest N reports
        recent_reports = report_files[:reports_to_match]
        
        # Extract timestamps from reports
        report_timestamps = [get_file_timestamp(r) for r in recent_reports]
        
        # Create folders for each report timestamp if they don't exist
        for timestamp in report_timestamps:
            folder_name = timestamp.strftime('%Y-%m-%d_%H-%M-%S')
            folder_path = os.path.join(SCREENSHOTS_DIR, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        
        # Move unorganized screenshots to appropriate folders based on timestamp
        for screenshot in screenshot_files:
            screenshot_timestamp = get_file_timestamp(screenshot)
            
            # Find the closest report timestamp
            closest_timestamp = None
            min_diff = float('inf')
            
            for report_timestamp in report_timestamps:
                diff = abs((screenshot_timestamp - report_timestamp).total_seconds())
                if diff < min_diff:
                    min_diff = diff
                    closest_timestamp = report_timestamp
            
            # If we found a close timestamp and it's within a reasonable time (1 hour)
            if closest_timestamp and min_diff < 3600:
                folder_name = closest_timestamp.strftime('%Y-%m-%d_%H-%M-%S')
                folder_path = os.path.join(SCREENSHOTS_DIR, folder_name)
                target_path = os.path.join(folder_path, os.path.basename(screenshot))
                
                try:
                    shutil.move(screenshot, target_path)
                    print(f"Moved screenshot {os.path.basename(screenshot)} to {folder_name}")
                except Exception as e:
                    print(f"Error moving screenshot {screenshot}: {e}")
            else:
                # If not matching any recent report, delete it
                try:
                    os.remove(screenshot)
                    print(f"Deleted unmatched screenshot: {os.path.basename(screenshot)}")
                except Exception as e:
                    print(f"Error deleting screenshot {screenshot}: {e}")
        
        # Remove any folders that don't match recent report timestamps
        timestamp_folders = [d for d in os.listdir(SCREENSHOTS_DIR) 
                           if os.path.isdir(os.path.join(SCREENSHOTS_DIR, d))]
        
        valid_folder_names = [t.strftime('%Y-%m-%d_%H-%M-%S') for t in report_timestamps]
        
        for folder in timestamp_folders:
            if folder not in valid_folder_names:
                folder_path = os.path.join(SCREENSHOTS_DIR, folder)
                try:
                    shutil.rmtree(folder_path)
                    print(f"Removed old screenshot folder: {folder}")
                except Exception as e:
                    print(f"Error removing folder {folder_path}: {e}")
    else:
        print(f"Unknown cleanup option: {option}")

def run_cleanup(max_reports=5, screenshot_option="match_reports", 
               max_screenshots=None, reports_to_match=5):
    """
    Run the cleanup process for both reports and screenshots
    
    Args:
        max_reports: Maximum number of reports to keep
        screenshot_option: "last_execution" or "match_reports"
        max_screenshots: Number of screenshots to keep (for last_execution)
        reports_to_match: Number of reports to match screenshots with (for match_reports)
    """
    print("Running cleanup process...")
    
    # Clean up reports
    cleanup_reports(max_reports)
    
    # Clean up screenshots
    cleanup_screenshots(screenshot_option, max_screenshots, reports_to_match)
    
    print("Cleanup completed.") 