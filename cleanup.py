#!/usr/bin/env python3
import argparse
from utilities.cleanup_utils import run_cleanup

def main():
    """
    Main function to parse command line arguments and run cleanup
    """
    parser = argparse.ArgumentParser(description='Clean up test reports and screenshots')
    parser.add_argument('--reports', type=int, default=5,
                        help='Number of recent reports to keep (default: 5)')
    parser.add_argument('--screenshots', choices=['last_execution', 'match_reports'], 
                        default='match_reports',
                        help='Screenshot cleanup strategy (default: match_reports)')
    parser.add_argument('--max-screenshots', type=int, default=None,
                        help='Number of recent screenshots to keep (default: all from last execution)')
    parser.add_argument('--reports-to-match', type=int, default=5,
                        help='Number of reports to match screenshots with (default: 5)')
    
    args = parser.parse_args()
    
    run_cleanup(
        max_reports=args.reports,
        screenshot_option=args.screenshots,
        max_screenshots=args.max_screenshots,
        reports_to_match=args.reports_to_match
    )

if __name__ == "__main__":
    main() 