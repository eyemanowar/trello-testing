# Trello Testing Framework

A comprehensive Python automation framework for testing Trello's REST API and web UI, combining API-driven test data setup with Selenium-based UI verification.

## Features

- **Hybrid Testing Approach**: API calls for fast test setup + Selenium for UI validation
- **Pytest Framework**: Professional test structure with fixtures and markers
- **Page Object Model**: Maintainable UI automation architecture
- **Helper Utilities**: Reusable components for boards, cards, lists
- **Configuration Management**: Environment-based config handling
- **Custom Test IDs**: Organized test case tracking with `@pytest.mark.tcid`

## Tech Stack

- **Python 3.10+**
- **pytest**: Test framework
- **Selenium**: Web automation
- **requests**: REST API testing
- **Page Object Model**: Design pattern

## Project Structure

```
trello-testing/
├── pytest.ini              # Pytest configuration
├── env.sh                  # Environment variables
├── tests/
│   ├── conftest.py         # Shared fixtures (WebDriver setup)
│   ├── test_board_test.py  # Board operations tests
│   └── test_cards_lists.py # Card and list tests
├── src/
│   ├── api_helpers/        # API integration layer
│   │   ├── board_helper.py # Board CRUD operations
│   │   └── card_helper.py  # Card operations
│   ├── page_helpers/       # Page Object Model
│   │   ├── list_page.py    # List page interactions
│   │   ├── card_page.py    # Card page interactions
│   │   └── board_not_found_page.py
│   ├── browser_helpers/    # WebDriver utilities
│   ├── configs/            # Configuration management
│   └── utilities/          # Generic utilities
│       ├── request_utility.py      # API request wrapper
│       └── generic_utilities.py    # String generation, etc.
└── data/
    ├── cookies.pkl         # Session persistence
    └── cookies_dump.json   # Session backup
```

## Key Components

### API Helpers
**Purpose**: Fast test data setup via Trello REST API

```python
# board_helper.py
class BoardHelper:
    def get_random_board()    # Get existing board for tests
    def get_random_list()     # Get list from board
    
# card_helper.py  
class CardHelper:
    def get_random_card()     # Get existing card for tests
```

### Page Object Model
**Purpose**: Maintainable UI automation with reusable page objects

```python
# list_page.py
class ListPage:
    def list_names()          # Extract all list names from board
    
# card_page.py
class CardPage:
    @property
    def card_name()           # Get card title from UI
```

### Request Utility
**Purpose**: Centralized API communication with authentication

```python
class RequestUtility:
    def get(endpoint, params)
    def post(endpoint, params)
    def put(endpoint, params)
    def delete(endpoint)
```

## Test Examples

### Test: Create List (API + UI Verification)
```python
@pytest.mark.tcid4
def test_create_list(driver):
    # 1. Setup: Get random board via API
    board = BoardHelper().get_random_board()
    
    # 2. Action: Create list via API
    payload = {'name': generate_custom_string()}
    rs_api = RequestUtility().post(f"boards/{board['id']}/lists", payload)
    
    # 3. Verify API response
    assert rs_api['name'] == payload['name']
    
    # 4. Verify UI with Selenium
    page = ListPage(driver)
    page.go(board['url'])
    assert payload['name'] in page.list_names()
```

### Test: Delete Card (API + UI Verification)
```python
@pytest.mark.tcid6
def test_delete_card(driver):
    # 1. Setup: Get existing card
    card = CardHelper().get_random_card()
    
    # 2. Action: Delete via API
    RequestUtility().delete(f"cards/{card['id']}")
    
    # 3. Verify: Navigate to card URL
    page = NotFoundPage(driver)
    page.go(card['url'])
    
    # 4. Assert: Confirm deletion
    assert page.not_found_h1.text == 'Card not found.'
```

## Setup

### 1. Install Dependencies
```bash
pip install pytest selenium requests
```

### 2. Configure Environment Variables
```bash
# env.sh
export TRELLO_API_KEY='your_api_key'
export TRELLO_TOKEN='your_token'
export BROWSER='chrome'  # or 'firefox'

source env.sh
```

### 3. WebDriver Setup
- Chrome: Install [ChromeDriver](https://chromedriver.chromium.org/)
- Firefox: Install [GeckoDriver](https://github.com/mozilla/geckodriver)

Add to PATH or specify in `conftest.py`

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test by ID
```bash
pytest -m tcid4  # Run test_create_list
pytest -m tcid5  # Run test_create_card
```

### Run with Verbose Output
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest tests/test_cards_lists.py
```

## Test Architecture Benefits

### Hybrid Approach
- **API for Setup**: Fast test data creation (boards, lists, cards)
- **UI for Verification**: Real user experience validation
- **Best of Both**: Speed of API + confidence of UI testing

### Page Object Model Benefits
- **Maintainability**: UI changes isolated to page objects
- **Reusability**: Common actions shared across tests
- **Readability**: Tests read like business workflows

### Helper Pattern Benefits
- **Abstraction**: Hide API complexity from tests
- **Randomization**: `get_random_*` methods for varied test data
- **Flexibility**: Easy to extend with new helper methods

## Configuration

### pytest.ini
```ini
[pytest]
markers =
    tcid4: Create list test
    tcid5: Create card test
    tcid6: Delete card test
    tcid7: Update list test
```

## Cookie Management

Session cookies stored for faster test execution:
- `cookies.pkl`: Pickled session data
- `cookies_dump.json`: Human-readable backup

## Logging

- `bmp.log`: Browser proxy logs
- `server.log`: Test execution logs

## Test Coverage

Current test scenarios:
- ✅ Create list (API + UI)
- ✅ Create card (API + UI)
- ✅ Delete card (API + UI)
- ✅ Update list name (API + UI)

## Future Enhancements

- [ ] CI/CD integration (GitHub Actions)
- [ ] Parallel test execution
- [ ] Screenshot capture on failure
- [ ] HTML test reports
- [ ] Test data cleanup fixtures
- [ ] Additional coverage: board operations, attachments, labels
- [ ] Performance testing with load scenarios
- [ ] Cross-browser testing matrix

## Best Practices Demonstrated

1. **Separation of Concerns**: Tests, page objects, API helpers, utilities
2. **DRY Principle**: Reusable helpers and fixtures
3. **Clear Test Structure**: Arrange-Act-Assert pattern
4. **Explicit Waits**: (implement in page objects for stability)
5. **Configuration Management**: Environment-based settings
6. **Test Isolation**: Independent test cases

## Troubleshooting

### WebDriver Issues
```bash
# Verify driver in PATH
which chromedriver

# Update to match browser version
```

### API Authentication
```bash
# Verify credentials
echo $TRELLO_API_KEY
echo $TRELLO_TOKEN
```

## License

Personal project - educational purposes

## Author

Oleksii Kolumbet

---

**Framework Highlights for CV:**
- Hybrid API + UI testing architecture
- Page Object Model implementation
- Pytest framework with custom markers
- REST API integration with helper pattern
- Reusable test components and utilities
