# Best Practices for Incident Response and Breach Notification under HIPAA/HITECH

## Overview

A security incident is a attempted or successful unauthorized access, use, disclosure, modification, or destruction of information or interference with system operations. A **breach** is a specific type of incident defined as the unauthorized acquisition, access, use, or disclosure of PHI that compromises the security or privacy of the information. A swift, organized, and legally compliant response is critical to mitigating damage and regulatory penalties.

## Phase 1: Preparation (Before an Incident Occurs)

### 1. Develop a Robust Incident Response Plan (IRP)
*   **Best Practice:** Have a written, approved plan in place. It should be actionable, not just a policy document.
*   **Key Components of an IRP:**
    *   **Team Roster:** Clearly define the Incident Response Team with roles, responsibilities, and 24/7 contact information. Include IT, compliance/legal, HR, PR, and senior management.
    *   **Definitions:** Provide clear definitions of an "incident" and a "breach" based on HIPAA/HITECH.
    *   **Response Procedures:** Step-by-step guides for containment, eradication, and recovery.
    *   **Communication Plan:** Templates for internal communications and external notifications (patients, HHS, media).
    *   **Forensics and Documentation:** Procedures for preserving evidence and documenting every action taken.

### 2. Conduct Training and Tabletop Exercises
*   **Best Practice:** Train the IR team on the plan and conduct simulated breach scenarios (tabletop exercises) at least annually. This tests the plan and reveals gaps.

## Phase 2: Identification and Containment

### 1. Detect and Triage
*   **Best Practice:** Use monitoring tools and user reports to identify potential incidents quickly.
*   **Action:** The first person aware of the incident should know to immediately contact the pre-defined IR team lead.

### 2. Activate the Team and Contain the Threat
*   **Best Practice:** The IR team lead activates the plan. The immediate priority is to **contain the damage**.
*   **Containment Actions:** May include disconnecting a compromised system from the network, disabling accounts, revoking access, or taking a server offline.

## Phase 3: Assessment and Breach Risk Analysis

### 1. Perform a Forensics Investigation
*   **Best Practice:** Engage legal counsel and a third-party digital forensics firm if the incident is complex. This helps maintain attorney-client privilege.
*   **Goal:** Determine the scope, root cause, and what PHI was involved (whose, what type, etc.).

### 2. Conduct the Mandatory Breach Risk Assessment
*   **Best Practice:** For any incident involving unauthorized PHI access, perform a formal assessment to determine if a breach occurred. Document the entire assessment.
*   **The Four Factors to Assess (Per HIPAA):**
    1.  **Nature and Extent of PHI:** What data was involved? Was it sensitive? (e.g., HIV status vs. a name alone).
    2.  **Unauthorized Person:** Who accessed the PHI? Was it another covered entity bound by HIPAA or a malicious external actor?
    3.  **Acquisition or Viewing:** Was the PHI actually viewed or acquired, or was it merely exposed but likely not accessed?
    4.  **Mitigation:** Have you mitigated the risk? (e.g., obtained signed confidentiality assurances from the internal person who mishandled it).

*   **Presumption of Breach:** If the assessment cannot demonstrate a **low probability** that the PHI was compromised, you must presume a breach occurred and begin notification procedures.

## Phase 4: Notification

If a breach is confirmed, strict timelines apply.

### 1. Notify Individuals
*   **Timeline:** Without unreasonable delay, **no later than 60 calendar days** after discovery.
*   **Method:** By first-class mail (or email if the individual has agreed). If contact information is out-of-date, make a reasonable attempt (e.g., phone call). If 10 or more individuals have outdated info, must post a notice on the website homepage for 90 days or provide notice to major media outlets.
*   **Content:** Must be written in plain language and include:
    *   A description of the breach.
    *   The types of information involved.
    *   Steps individuals should take to protect themselves.
    *   A description of what the entity is doing to investigate and mitigate harm.
    *   Contact information for questions.

### 2. Notify the Secretary of HHS
*   **Timeline:**
    *   **>500 individuals:** Notify simultaneously with individual notices.
    *   **<500 individuals:** Log the breach and notify HHS within 60 days after the end of the calendar year.
*   **Method:** Submit electronically through the OCR breach portal.

### 3. Notify the Media (Only for large breaches)
*   **Timeline:** Without unreasonable delay, **no later than 60 calendar days** after discovery.
*   **Trigger:** A breach affecting more than 500 residents of a single state or jurisdiction.
*   **Method:** Issue a press release to prominent media outlets serving the affected area.

## Phase 5: Post-Incident Activity

### 1. Perform Root Cause Analysis
*   **Best Practice:** After the immediate crisis, hold a "lessons learned" meeting. What allowed the incident to happen? Was it a technical failure, a process failure, or a human error?

### 2. Update Policies and Procedures
*   **Best Practice:** Use the findings from the root cause analysis to update security measures, policies, and training to prevent a similar incident from recurring. This demonstrates a culture of continuous improvement to regulators.