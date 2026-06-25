# Helpline Videos — Shot List

Short screen-recordings, one task each, that the chatbot returns alongside its text answer.

## Recording rules (keep clips reusable)
- **One task per clip**, 20–60 seconds. No intro/outro fluff — start on the relevant screen, do the task, done.
- **Use a TEST patient**, never real patient data (these clips may be shown to many people).
- Consistent screen size and zoom; mouse movements slow and deliberate; highlight/click clearly.
- **Naming = the clip ID below**, e.g. `smbg-report.mp4`. Save them all in one `videos/` folder.
- Silent screen-capture is fine (the text answer explains it); voiceover optional.
- Re-record a clip if the UI changes — the ID stays the same so the mapping never breaks.

## How it plugs into the agent (so naming matters)
Each clip ID matches a question in the knowledge base. Once recorded, I add a `video:` line to each
Q&A entry, and the agent appends "▶ Watch: <link>" under the steps. So if you record `assign-package.mp4`,
the "How do I assign a package?" answer automatically shows that clip.

---

## TIER 1 — record these first (most-asked)

1. **`dashboard-tour.mp4`** — First-login overview tour: the sidebar (Overview, Patients, Chats, Packages,
   Care Providers, Exercises, Gamification) and what the Overview screen shows. *Answers: "I just logged in, what is this / give me a tour."*
2. **`find-and-open-patient.mp4`** — Search a patient by name/phone, then open them via the row ⋮ → View
   (note: clicking the name only selects the row). *Answers: "how do I open a patient / find a patient."*
3. **`smbg-report.mp4`** — Patient ⋮ → Reports → SMBG tab → pick a range (e.g. This Week). *Answers: "where is the SMBG report."*
4. **`cgm-glucose-stats.mp4`** — Patient → Reports → CGM → set start/end dates → View Report (time in range, average, variability). *Answers: "blood glucose statistics."*
5. **`assign-package.mp4`** — Open patient → Assign Package → choose package + start date → Submit. *Answers: "assign a package."*
6. **`chat-with-documents.mp4`** — Enable the Documents chip → scroll to Documents → tick docs → click Chat. *Answers: "chat with documents."*
7. **`upload-patient-data.mp4`** — Upload button → choose Data Type (LibreView CSV / Reports / etc.) → drag & drop file. *Answers: "upload CGM data / add a document."*
8. **`cgm-not-syncing.mp4`** — Left panel → Connected Apps (LibreView) → check Last Sync → Sync Now. *Answers: "glucose isn't syncing."*
9. **`toggle-chips.mp4`** — Show that Documents/Notifications are toggle chips; enable a hidden section. *Answers: "I can't find a tab/section."*

## TIER 2 — common daily tasks

10. **`add-prescription.mp4`** — Medications section → Add Prescription. *Answers: "add a medication/prescription."*
11. **`create-diet-plan.mp4`** — Left panel bottom → Diet Plans → Create. *Answers: "create a diet plan."*
12. **`read-meal-report.mp4`** — Day Report → Meal Report: kcal ring, macros, meal cards. *Answers: "see what a patient ate / meal report."*
13. **`read-fitness-report.mp4`** — Day Report → Fitness Report: steps, active energy, steps-by-hour. *Answers: "see activity/steps."*
14. **`proactive-insights.mp4`** — Proactive Insights section + Refresh. *Answers: "what are proactive insights."*
15. **`notifications.mp4`** — Notifications section: unread filter + category chips. *Answers: "where are patient notifications."*
16. **`research-module.mp4`** — Research chip → tour Overview + domain tabs (Metabolic, Cardiovascular, …). *Answers: "what is Research / deep health metrics."*
17. **`export-patient.mp4`** — Export button on the patient profile. *Answers: "export a patient's data."*
18. **`filter-patients.mp4`** — Patients → Filters → Monitoring Method = SMBG (and Package = No Package). *Answers: "find all SMBG patients / patients without a package."*

## TIER 3 — admin / setup tasks

19. **`add-patient.mp4`** — Patients → Add New → fill Basic Info steps. *Answers: "add a new patient."*
20. **`add-care-provider.mp4`** — Care Providers → Add New → Personal Info (with Role) → Medical Info. *Answers: "add a care provider."*
21. **`manage-provider-permissions.mp4`** — Care Providers → ⋮ → Manage Permissions → CRUD toggles → Save. *Answers: "give/restrict provider access."*
22. **`share-invite-code.mp4`** — Care Providers ⋮ → Share Invite Code (and Packages ⋮ → Share Join Code). *Answers: "invite a provider / join code."*
23. **`create-package.mp4`** — Packages → Add New → name, type, duration, price. *Answers: "create a package."*
24. **`message-a-patient.mp4`** — Chats → pick conversation → send a message. *Answers: "message a patient."*
25. **`overview-triage.mp4`** — Overview: At-Risk Patients, Hyper/Hypo/High GV cards, Patient Risk Records. *Answers: "see at-risk patients / glucose events across everyone."*

## TIER 4 — nice to have

26. **`exercises-search-filter.mp4`** — Exercises → search + Filters (level/category/muscle/equipment). *Answers: "find an exercise."*
27. **`add-exercise.mp4`** — Exercises → Add New. *Answers: "add a custom exercise."*
28. **`gamification-create-group.mp4`** — Gamification → Groups → Create Group. *Answers: "set up a group."*
29. **`gamification-create-challenge.mp4`** — Gamification → Challenges → Create Challenge. *Answers: "create a challenge."*
30. **`health-agent.mp4`** — Open the floating Health Agent; show it answers patient-DATA questions (vs. this how-to bot). *Answers: "what's the robot icon / how do I ask about a patient's data."*

---

## Suggested folder
Save recordings here: `~/Desktop/dashboard-helpline-agent/videos/`
(Filenames exactly as the IDs above, `.mp4`.) When some are ready, tell me and I'll wire them into the answers.
