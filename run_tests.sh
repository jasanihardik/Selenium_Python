#!/bin/bash

# Colors for console output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Help message
function show_help {
    echo -e "${BLUE}WebDriverUniversity Test Runner${NC}"
    echo "This script runs automated tests for WebDriverUniversity website."
    echo ""
    echo "Usage: ./run_tests.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -a, --all                  Run all tests"
    echo "  -t, --test TEST_FILE       Run a specific test file"
    echo "  -m, --module MODULE        Run tests in a specific module (contact_us, login, etc.)"
    echo "  -c, --case TEST_CASE       Run a specific test case (requires -m)"
    echo "  -b, --browser BROWSER      Specify browser (chrome, firefox, edge)"
    echo "  -h, --headless             Run in headless mode"
    echo "  --no-cleanup               Skip cleanup of old reports and screenshots"
    echo "  --help                     Display this help message"
    echo ""
    echo "Examples:"
    echo "  ./run_tests.sh --all                         # Run all tests"
    echo "  ./run_tests.sh -t test_login.py              # Run a specific test file"
    echo "  ./run_tests.sh -m login                      # Run all login tests"
    echo "  ./run_tests.sh -m contact_us -c test_successful_submission  # Run a specific test case"
    echo "  ./run_tests.sh -a -b firefox                 # Run all tests in Firefox"
    echo "  ./run_tests.sh -m dropdown -h                # Run dropdown tests in headless mode"
    echo "  ./run_tests.sh -a --no-cleanup              # Run all tests without cleaning up old reports"
    echo ""
}

# Default values
ALL_TESTS=false
TEST_FILE=""
MODULE=""
TEST_CASE=""
BROWSER="chrome"
HEADLESS=false
CLEANUP=true

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -a|--all)
            ALL_TESTS=true
            shift
            ;;
        -t|--test)
            TEST_FILE="$2"
            shift 2
            ;;
        -m|--module)
            MODULE="$2"
            shift 2
            ;;
        -c|--case)
            TEST_CASE="$2"
            shift 2
            ;;
        -b|--browser)
            BROWSER="$2"
            shift 2
            ;;
        -h|--headless)
            HEADLESS=true
            shift
            ;;
        --no-cleanup)
            CLEANUP=false
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Error: Unknown option $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# Validate input parameters
if [[ "$TEST_CASE" != "" && "$MODULE" == "" ]]; then
    echo -e "${RED}Error: A module (-m) must be specified when using a test case (-c)${NC}"
    exit 1
fi

if [[ "$ALL_TESTS" == "false" && "$TEST_FILE" == "" && "$MODULE" == "" ]]; then
    echo -e "${YELLOW}No test selection specified. Showing help message:${NC}"
    show_help
    exit 1
fi

# Set up headless argument if needed
HEADLESS_ARG=""
if [[ "$HEADLESS" == "true" ]]; then
    HEADLESS_ARG="--headless=true"
fi

# Build the pytest command
PYTEST_CMD="python3 -m pytest"

# Add browser parameter
PYTEST_CMD="$PYTEST_CMD --browser-name=$BROWSER"

# Add headless parameter if needed
if [[ "$HEADLESS" == "true" ]]; then
    PYTEST_CMD="$PYTEST_CMD --headless=true"
fi

# Add tests to run
if [[ "$ALL_TESTS" == "true" ]]; then
    PYTEST_CMD="$PYTEST_CMD tests/test_cases/"
elif [[ "$TEST_FILE" != "" ]]; then
    # Check if the file has a .py extension
    if [[ "$TEST_FILE" != *.py ]]; then
        TEST_FILE="$TEST_FILE.py"
    fi
    
    # Check if the file exists
    if [[ ! -f "tests/test_cases/$TEST_FILE" ]]; then
        echo -e "${RED}Error: Test file tests/test_cases/$TEST_FILE does not exist${NC}"
        exit 1
    fi
    
    PYTEST_CMD="$PYTEST_CMD tests/test_cases/$TEST_FILE"
elif [[ "$MODULE" != "" ]]; then
    # Check if the file has a .py extension
    if [[ "$MODULE" != *.py ]]; then
        MODULE="test_$MODULE.py"
    elif [[ "$MODULE" != test_* ]]; then
        MODULE="test_$MODULE"
    fi
    
    # Check if the file exists
    if [[ ! -f "tests/test_cases/$MODULE" ]]; then
        echo -e "${RED}Error: Module file tests/test_cases/$MODULE does not exist${NC}"
        exit 1
    fi
    
    if [[ "$TEST_CASE" == "" ]]; then
        PYTEST_CMD="$PYTEST_CMD tests/test_cases/$MODULE"
    else
        # Extract the class name from the module file
        CLASS_NAME=$(grep -m 1 "class Test" "tests/test_cases/$MODULE" | sed -E 's/class ([^:]+):.*/\1/')
        
        # Check if test case exists in the module
        if ! grep -q "def $TEST_CASE" "tests/test_cases/$MODULE"; then
            echo -e "${RED}Error: Test case $TEST_CASE not found in tests/test_cases/$MODULE${NC}"
            exit 1
        fi
        
        # Extract module name without extension
        MODULE_NAME=$(basename "$MODULE" .py)
        
        PYTEST_CMD="$PYTEST_CMD tests/test_cases/$MODULE::$CLASS_NAME::$TEST_CASE"
    fi
fi

# Add HTML report parameter
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_NAME="test_report_$TIMESTAMP.html"
PYTEST_CMD="$PYTEST_CMD -v --html=reports/$REPORT_NAME --self-contained-html"

# Create reports directory if it doesn't exist
mkdir -p reports

# Display the command
echo -e "${BLUE}Executing:${NC} $PYTEST_CMD"

# Run the tests
eval $PYTEST_CMD
EXIT_CODE=$?

# Show the report location
if [[ $EXIT_CODE -eq 0 ]]; then
    echo -e "${GREEN}Tests completed successfully!${NC}"
else
    echo -e "${RED}Tests completed with failures!${NC}"
fi

echo -e "${BLUE}Report saved to:${NC} reports/$REPORT_NAME"
echo -e "${BLUE}Full path:${NC} $(pwd)/reports/$REPORT_NAME"

# Run cleanup if enabled
if [[ "$CLEANUP" == "true" ]]; then
    echo -e "${BLUE}Running cleanup to keep last 5 reports and organize screenshots...${NC}"
    python3 cleanup.py --screenshots match_reports
fi

exit $EXIT_CODE 