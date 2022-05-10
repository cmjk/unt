## General ideas

1. Think about testing during feature planning, before any code is written
2. Test before you push the changes to production (we need at least another environment for that)
3. If you do have to test in production, do it off-peak hours (2-4 AM?)
4. It's generally a good idea to do a post-mortem when a bug is found in production (with the goal being to understand
   which changes can be made to the QA process in the team, so that this type of issue is prevented)
5. Try to avoid half-implementing features, it will cause frustration for the users (e.g. wireframe says to leave the
   list icon without any function should it be clicked)

## Bugs

- Sorting by name is not applied
- List view was implemented, but should not have (IMO, should not have been part of the wireframe)
- Subcategories are not sorted alphabetically
- For HP ENVY, the description is from another item
- Build your own PC price misleading (if you go to the product, price is higher than on search results page)
- Actual minimum search term is 3 symbols
- Display per page options don't match wireframe

## QA challenges

- Planning: ideally, test cases should exist before a feature is in production
- Documentation: needed to fully understand what is expected of the search API
- Data: not enough data exists to test some search features fully, we need a mechanism to generate products quickly.

## Product suggestions

- Reconsider the value of searching top-level categories in advanced search. A product will never be part of the
  results, only categories. Consider enabling subcategory search at all times, and removing the toggle. Minimize the
  number of clicks to get to a product.
- We only have 3 manufacturers currently, instead of the View All button, we could show the 3rd manufacturer.
