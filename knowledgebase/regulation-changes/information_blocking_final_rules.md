# 21st Century Cures Act: Information Blocking and API Rules

## Change Notice Summary

*   **Regulation Affected:** 21st Century Cures Act (Title IV, Section 4004)
*   **Issuing Agencies:** The Office of the National Coordinator for Health IT (ONC) and the Centers for Medicare & Medicaid Services (CMS)
*   **Final Rule Date:** March 9, 2020
*   **Compliance Deadlines:** Staggered between 2020 and 2023 (see below).
*   **Status:** Active Enforcement for some provisions; future deadlines for others.

## Overview of the Change

The 21st Century Cures Act, passed in 2016, aimed to accelerate medical product development and innovation. A critical provision, aimed at improving patient access and interoperability, targeted "information blocking." The ONC and CMS Final Rules, published in 2020, defined these practices and established penalties for "actors" who engage in them. The goal is to ensure patients and their providers have seamless access to electronic health information (EHI).

## Key Changes and Amendments

### 1. Definition of Information Blocking

*   **Definition:** A practice by an "actor" that is likely to interfere with, prevent, or materially discourage access, exchange, or use of electronic health information (EHI).
*   **Actors:** The rule applies to:
    *   Healthcare Providers
    *   Health Information Networks (HINs) / Health Information Exchanges (HIEs)
    *   Certified Health IT Developers (e.g., EHR vendors)
*   **Exceptions:** The rule defines eight exceptions that are *not* considered information blocking. These are activities that, while they might interfere with access, are reasonable and necessary to promote another policy objective (e.g., privacy, security, preventing harm).

### 2. Expansion of EHI and USCDI

*   **Change:** The definition of what data must be shared was expanded beyond the traditional "designated record set" in HIPAA. It now aligns with the **United States Core Data for Interoperability (USCDI)** standard, which includes clinical notes, allergies, lab results, and more.
*   **Impact:** Organizations must ensure their systems can access and export this broader set of data elements.

### 3. API Requirements ("Patient Access API" and "Provider Directory API")

*   **Change:** The rules require certified health IT to provide standardized, secure application programming interfaces (APIs). This enables patients to access their data through third-party apps of their choice (with proper security and privacy credentials) using the FHIR (Fast Healthcare Interoperability Resources) standard.
*   **Impact:** This creates a "health data economy" where patients can aggregate their data from multiple sources into apps for managing their health. Providers and IT developers must build and maintain these APIs.

### 4. Enforcement and Penalties

*   **For Providers:** Enforcement is through CMS's "Conditions of Participation." Engaging in information blocking could affect a hospital's or provider's ability to participate in Medicare and Medicaid. CMS has also established a public complaint process.
*   **For Health IT Developers/HINs/HIEs:** Enforcement is through the Office of Inspector General (OIG), which can impose civil monetary penalties of up to **$1 million per violation**.

## Key Deadlines (Past and Future)

*   **April 5, 2021:** Information Blocking provisions went into effect for actors.
*   **October 6, 2022:** The scope of EHI that must be shared expanded to the full USCDI v1 standard.
*   **Future:** Deadlines for implementing newer versions of USCDI and other API requirements are ongoing.

## Action Items for Compliance

1.  **Conduct an Information Blocking Audit:** Review internal policies and practices (e.g., fees for record release, data exchange processes, third-party app access) to ensure they don't constitute blocking.
2.  **Understand the Exceptions:** Familiarize yourself with the eight exceptions to justify any practice that might limit data sharing.
3.  **Ensure API Capability:** For IT developers, ensure products are certified and APIs are functional. For providers, understand how to leverage these APIs for patient care.
4.  **Update Patient Access Procedures:** Develop a streamlined process for responding to patient requests for access to their EHI via apps and other digital means.
5.  **Train Staff:** Ensure all relevant workforce members, from front-desk staff to clinicians and IT, understand what information blocking is and how to avoid it.