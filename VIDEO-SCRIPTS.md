# Helpline Videos — Recording Scripts (click-by-click)

A storyboard for each of the 30 clips. Each = one task, 20–60s.
Format: **START** (where to be before you hit record) → numbered actions → **SHOW** (what to linger on) → **END**.

## Before every recording
- Log in first; be on the screen listed under START before you press record.
- Use a **TEST patient** (no real patient data on screen).
- Browser at ~100% zoom, window a consistent size. Move the mouse slowly; pause ~1s after each click.
- No need to talk — the chatbot's text explains the steps. Optional captions are in *italics*.
- Save as the exact filename shown, into `~/Desktop/dashboard-helpline-agent/videos/`.

---

# TIER 1

## 1. dashboard-tour.mp4
**START:** Overview page (just after login).
1. Slowly move down the left sidebar, hovering each item: Overview → Patients → Chats → Packages → Care Providers → Exercises → Gamification.
2. Back on Overview, pan across the top stat cards (Active Patients, Patients Enrolled, Meals Uploaded, At-Risk Patients).
3. Scroll down to the Hyper / Hypo / High GV event cards.
4. Scroll to Patient Risk Records, then the Activity & Nutrition panel (Step Counts / Macro Nutrition tabs).
**SHOW:** that the sidebar is how you move around; Overview is the home screen.
**END:** back at top of Overview.

## 2. find-and-open-patient.mp4
**START:** Patients page.
1. Click the search bar, type a test patient's name (or phone).
2. *Caption: "Clicking the name only ticks the row — use the menu."*
3. Click the **⋮ (three dots)** in that row's Actions column.
4. Click **View**.
**SHOW:** the patient profile loading.
**END:** patient profile open.

## 3. smbg-report.mp4
**START:** a test patient's profile.
1. Click the purple **Reports** button (top-left). *(Or from the list: row ⋮ → Reports.)*
2. In the popup, click the **SMBG** tab (next to CGM and Diet).
3. Click a quick range, e.g. **This Week**.
**SHOW:** the SMBG report opening.
**END:** report visible.

## 4. cgm-glucose-stats.mp4
**START:** a test patient's profile.
1. Click **Reports** → click the **CGM** tab.
2. Set the **Start Date** and **End Date**.
3. Click **View Report**.
4. *(Optional second half)* Close it, go to **Day Report → CGM Report** sub-tab and pick a day to show the daily glucose curve.
**SHOW:** the period stats (time in range / average / variability) and the daily curve.
**END:** report visible.

## 5. assign-package.mp4
**START:** a test patient's profile.
1. Click the orange **Assign Package** button (top-left).
2. Open the **Package** dropdown and pick one (e.g. CGM-AiHealth).
3. Set a **Start Date**.
4. Click **Submit**.
**SHOW:** the confirmation / the package now assigned.
**END:** back on the profile.

## 6. chat-with-documents.mp4
**START:** a test patient's profile that HAS a couple of documents uploaded.
1. At the top, make sure the **Documents** chip is on (click it if it's grey).
2. Scroll to the **Documents** section.
3. Tick the checkboxes of 1–2 documents (max 10). *Caption: "Select up to 10."*
4. Click the **Chat** button.
5. Type a sample question like "Summarize this report" and send.
**SHOW:** the "N selected" counter changing, then the AI answering about the docs.
**END:** answer shown.

## 7. upload-patient-data.mp4
**START:** a test patient's profile.
1. Click the green **Upload** button (top-left).
2. In "Upload Patient Data", open the **Data Type** dropdown — pause so all options show (LibreView Raw CSV, Linx Raw CSV, Sinocare Raw Excel, Reports, Other Medical Documents).
3. Pick one (e.g. LibreView Raw CSV, or "Reports" for a document).
4. Drag & drop a file into the drop area.
**SHOW:** the data type list and the file dropping in.
**END:** upload started / done; close the modal.

## 8. cgm-not-syncing.mp4
**START:** a test patient's profile.
1. In the left panel, scroll down to **Connected Apps** (e.g. LibreView).
2. Point to the **Last Sync** time.
3. Click **Sync Now**.
4. *Caption: "Still stuck? Unlink and relink here."* (hover Unlink, don't click).
**SHOW:** the sync action.
**END:** Connected Apps panel.

## 9. toggle-chips.mp4
**START:** a test patient's profile.
1. Point to the row of chips at the top (Day Report, Medications, Prescriptions, Documents, Proactive Insights, Notifications, Research).
2. Find a greyed-out chip (e.g. **Documents** or **Notifications**).
3. Click it — the section appears below.
4. Click it again — it disappears.
**SHOW:** chip turning blue/grey and the section showing/hiding. *Caption: "Missing a section? Turn its chip on."*
**END:** chip on, section visible.

---

# TIER 2

## 10. add-prescription.mp4
**START:** patient profile; enable the **Medications** chip and scroll to that section.
1. Click **Add Prescription**.
2. Fill in the fields the form shows (medication, dose, etc.).
3. Save.
4. Show it now appears under the **Active** tab; click **Prescription History** to show uploaded ones.
**SHOW:** the new medication in the list.
**END:** Medications section.

## 11. create-diet-plan.mp4
**START:** patient profile.
1. Scroll the left panel to the bottom to **Diet Plans**.
2. Click **Create**.
3. Walk through the create flow that appears and save.
**SHOW:** the new diet plan created.
**END:** Diet Plans section.

## 12. read-meal-report.mp4
**START:** patient profile, **Day Report → Meal Report**.
1. Pick a day on the week date-strip.
2. Show the kcal ring and the Carbs / Protein / Fats / Fiber cards.
3. Scroll to the **Meals** cards.
4. Click the **eye / view** icon on one meal to open its detail.
**SHOW:** macros and a meal's detail.
**END:** meal detail.

## 13. read-fitness-report.mp4
**START:** patient profile, **Day Report → Fitness Report** sub-tab.
1. Pick a day on the date-strip.
2. Show the Daily Activity Snapshot (Steps, Active Energy, Active Time, Peak hour).
3. Scroll to the **Steps by Hour** chart.
**SHOW:** the activity numbers and hourly chart.
**END:** chart visible.

## 14. proactive-insights.mp4
**START:** patient profile; enable the **Proactive Insights** chip.
1. Scroll to the Proactive Insights section.
2. Read across an insight card (badge, tag, title, body, suggested follow-up).
3. Click **Refresh**.
**SHOW:** an insight card and the refresh.
**END:** insights shown.

## 15. notifications.mp4
**START:** patient profile; enable the **Notifications** chip.
1. Scroll to the Notifications section; show the unread count.
2. Toggle **Unread only**.
3. Click through the category chips (Gamification, Med Lifecycle, Refill, Dose, Follow-up).
**SHOW:** filtering by unread and category.
**END:** notifications list.

## 16. research-module.mp4
**START:** a test patient's profile.
1. Click the **Research** chip (it opens the Research page).
2. On **Overview**, pan the Patient Health Overview (Time In Range, Daily Steps, etc.) and the "Key Health Metrics at a Glance" cards.
3. Click through the top tabs: Metabolic → Cardiovascular → Body Composition → (others).
**SHOW:** the breadth of the Research module.
**END:** a domain tab open.

## 17. export-patient.mp4
**START:** a test patient's profile.
1. Click the **Export** button (top-left).
2. Show whatever options/download appear.
**SHOW:** the export action.
**END:** back on profile.

## 18. filter-patients.mp4
**START:** Patients page.
1. Click **Filters**.
2. Under **Monitoring Method**, click **SMBG Patient**, then **Apply**.
3. Show the filtered list.
4. Reopen Filters → under **Package** click **No Package** → Apply.
5. Click **Clear Filters**.
**SHOW:** the list changing with each filter.
**END:** cleared list.

---

# TIER 3

## 19. add-patient.mp4
**START:** Patients page.
1. Click **Add New**.
2. Step 1 "Basic Info": fill First Name, Last Name, Email, Phone (with country code), Date of Birth, Gender.
3. Click **Next** and continue through the remaining steps.
4. Submit.
**SHOW:** the stepper and submission. *(Use fake details.)*
**END:** new patient created / list.

## 20. add-care-provider.mp4
**START:** Care Providers page.
1. Click **Add New**.
2. Step 1 "Personal Info": First Name, Last Name, Email, Phone, and pick a **Role** from the dropdown.
3. Click **Next** → Step 2 "Medical Info" → fill → Submit.
**SHOW:** the 2-step form. *(Use fake details.)*
**END:** provider list.

## 21. manage-provider-permissions.mp4
**START:** Care Providers page.
1. Click a provider's **⋮** → **Manage Permissions**.
2. Show the CRUD checkboxes per module (Meals, Reports, Fitness, Cgms, CareProviders, …).
3. Toggle a couple (e.g. turn off Delete for Reports).
4. Click **Save Changes**.
**SHOW:** the permission grid and toggling.
**END:** saved.

## 22. share-invite-code.mp4
**START:** Care Providers page.
1. Click a provider's **⋮** → **Share Invite Code**; show the code.
2. *(Second half)* Go to **Packages**, click a package's **⋮** → **Share Join Code**; show that code.
**SHOW:** where to grab invite/join codes.
**END:** code visible.

## 23. create-package.mp4
**START:** Packages page.
1. Click **Add New**.
2. In "Add Package", fill Name, Description, **Package Type** (PREMIUM/BASIC/TRIAL), Duration (days), Price.
3. Click **Submit**.
**SHOW:** the form and the new package in the list.
**END:** packages list.

## 24. message-a-patient.mp4
**START:** Chats page.
1. (Optional) use the search or the **Groups / Unread Only** filters.
2. Click a conversation to open it.
3. Type a message in the composer and **Send**.
**SHOW:** the message sending and the read receipt.
**END:** thread with the new message.

## 25. overview-triage.mp4
**START:** Overview page.
1. Point to the **At-Risk Patients** stat card.
2. Show the **Hyper / Hypo / High GV** event cards.
3. Scroll to **Patient Risk Records**; click the filter tabs (All / Hyper / Hypo / High GV).
**SHOW:** how to spot at-risk patients across everyone.
**END:** risk records table.

---

# TIER 4

## 26. exercises-search-filter.mp4
**START:** Exercises page.
1. Type a term in the search (e.g. a muscle or name).
2. Click **Filters**; pick a Level, Category, Muscle, and/or Equipment.
3. Click **Apply**; show the filtered list.
**SHOW:** searching and filtering the library.
**END:** filtered list.

## 27. add-exercise.mp4
**START:** Exercises page.
1. Click **Add New**.
2. Fill the exercise fields the form shows (name, category, level, equipment, muscles).
3. Save.
**SHOW:** the new exercise added.
**END:** exercises list.

## 28. gamification-create-group.mp4
**START:** Gamification → **Groups** tab.
1. Click **Create Group**.
2. Fill the fields and save.
3. Show the new group with its Invite Code and member count.
**SHOW:** group creation.
**END:** groups list.

## 29. gamification-create-challenge.mp4
**START:** Gamification → **Challenges** tab.
1. Click **Create Challenge**.
2. Fill the fields (Title, Metric, Target, Duration, Period, XP Reward).
3. Save.
**SHOW:** challenge creation.
**END:** challenges list.

## 30. health-agent.mp4
**START:** any test patient's page.
1. Click the floating **robot icon** (bottom-right).
2. Show the Health Agent panel: the **Threads** list on the left and the suggested prompts (Glucose overview, Meal impact, Time in range, Overnight patterns).
3. Type a data question (e.g. "What's this patient's time in range this week?") and send.
4. *Caption: "Health Agent answers questions about patient DATA — different from the how-to helpline bot."*
**SHOW:** the agent answering a data question.
**END:** answer shown.

---

## After recording
Drop the files (named exactly as above) into `videos/` and tell me which IDs are done.
I'll add a `video:` link to each matching Q&A so the bot returns the clip with its answer.
