0001 Purpose of This Repo
#########################

Status
******

**Draft**

Context
*******

edX performs compliance with government regulations by checking users against the Consolidated Screening List provided by the U.S. Department of Commerce (SDN and ISN lists) on B2C single purchases and B2C subscription purchases. In the future, commerce-coordinator will also need access to this logic. This sanctions service will be used by multiple services, serving as a replacement for the SDN check and fallback that lives in ecommerce, which is deprecated.

Decision
********

We will create a repository that will facilitate SDN checks, maintain local backups of the SDN list, and record positive hits for reference.

Consequences
************

TODO: Add what other things will change as a result of creating this repo.

.. This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones. A particular decision may have positive, negative, and neutral consequences, but all of them affect the team and project in the future.

Rejected Alternatives
*********************

TODO: If applicable, list viable alternatives to creating this new repo and give reasons for why they were rejected. If not applicable, remove section.

.. This section lists alternate options considered, described briefly, with pros and cons.

References
**********

`SDN Service Implementation <https://2u-internal.atlassian.net/wiki/spaces/RS/pages/546668614/SDN+Service+Implementation>`_
