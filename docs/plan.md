# Test Plan

## Unit testing

Devs testing pieces of their code

## Integration testing

To guarantee that the UI generates requests that the API can work with. This would allow us to offload some E2E tests
into the API layer.

For example, SORT BY functionality essentially controls the value of the parameter called ORDERBY in the search API
requests.

```
class OrderBy(Enum):
    ## values taken from the UI
    default = 0
    a_to_z = 5
    z_to_a = 6
    price_low_to_high = 10
    price_high_to_low = 11
    created_on = 15
```

If we can guarantee that these are indeed the correct values for these options, then instead of testing SORT BY in the
UI, we can do so by sending GET requests with different options, which is quicker and less prone to flakiness.

## API testing

Requests sent to the API by the UI (in the long-run, consider switching from server-side rendering to a JSON-based API)

In the context of the search function: test all parameters of the search API (documentation from the devs needed)

```
@dataclass
class SearchParams:
    q: str
    viewmode: str = "grid"
    orderby: int = 0
    pagesize: int = 18
    advs: bool = True
    cid: int = 0
    isc: bool = False
    mid: int = 0
    vid: str = ""
    sid: bool = True
```

From there, we can construct is URL to perform a GET request with. HTML can then be parsed to load products, and verify
against an expectation.

## Automated E2E testing

Here, the focus on high-level functional scenarios (if not automated, have to be run manually)

### search feature

- input field and search button are visible from the home page (automated)
- some query returns results (automated)
- sort by (automated) and display number of items (need more data) dropdowns modify output
- pagination: go to next/previous page, go directly to page number
- clicking product image or name takes user to product page (automated)
- minimum search term (automated)

### advanced search feature

- can filter by manufacturer
- can search in category
- can search in subcategory
- can use Automatically search sub categories checkbox

### UX

- list view should not be enabled
- dropdown options are displayed as designed

## Security

- sanitize user inputs in API parameters
