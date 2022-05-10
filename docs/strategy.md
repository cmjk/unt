# Test Strategy

| Testing Type  | Done by  | When                     |
|---------------|----------|--------------------------|
| Unit          | Devs     | During Feature dev       |
| Integration   | Devs     | During Feature dev       |
| Manual E2E    | QA       | During Feature dev       |
| Automated E2E | QA       | During/After feature dev |
| System        | Everyone | Before a release         |

## Environments:

### DEV

Feature branches are deployed to this environment with automated tests being part of the deployment process. Feature
testing is then performed.

### STAGING

A group of features developed over a period of time end up in a Release Candidate branch that is deployed to the staging
env, where system testing is performed. At this point, no new features code should be merged into the release branch,
only bugfixes.

### PROD

An RC branch that passed all checks is deployed to production during off-peak hours. A sanity check is performed (a
subset of test scenarios that focus on happy paths, plus some exploratory testing).

### The Data Issue

Before testing can start, an environment needs to be populated with test data (products, customer accounts and so on).
This process needs to be quick and reliable, ideally, we would restore some sort of 'gold' DB snapshot before running
tests. Tests that make modifications to the data need to restore the original state if that env is to be reused. We will
likely need scripts to populate the deployment with it on demand.

### Additionally

Performance testing (good to have if resources allow it, crucial to run before a marketing campaign, where we could
expect an influx of new users).

Accessibility testing (if time allows).

GDPR-compliance

Sensitive data storage
