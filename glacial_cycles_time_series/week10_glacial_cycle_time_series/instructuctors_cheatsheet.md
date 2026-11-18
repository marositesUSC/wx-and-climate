
# GEOG 202 Honors — Instructor Answer Key

Investigating Glacial and Interglacial Cycles with Python

## Part 1 — What is a cycle?


Q1: Run the plot with periods of 23, 41, and 100 kyr. Which completes the most cycles over 200 kyr?

• Answer: The 23-kyr period completes the most cycles (~8.7 cycles over 200 kyr, compared to ~4.9 cycles for 41 kyr and 2.0 cycles for 100 kyr).
• Key Concept: Shorter periods correspond to higher frequencies (f = 1/T), meaning more repetitions occur within a fixed time window.

### Q2: Which periods are present in this example?

• Answer: 23 kyr, 41 kyr, and 100 kyr (all three peaks appear clearly at ~23, ~41, and ~100 on the horizontal period axis with equal spectral power).

Discussion: Why might a climate record have more than one important period?

• Answer: Earth's climate responds simultaneously to multiple external drivers (such as different orbital cycles—precession, obliquity, and eccentricity) as well as internal Earth-system oscillators and feedbacks (ice-sheet dynamics, ocean circulation, and greenhouse gas cycles) that operate on distinct timescales.

## Part 2 — Milankovitch cycles and insolation


### Q3: Which parameter appears to vary fastest? Which varies slowest? Are these patterns perfectly regular?

• Answer:
	• Fastest: Precession (green, bottom panel), oscillating every ~19–23 kyr.
	• Slowest: Eccentricity (blue, top panel), varying over ~100 kyr and ~405 kyr cycles.
	• Regularity: No, they are not simple constant-amplitude sine waves—each parameter is modulated by multiple overlapping gravitational frequencies (for example, precession exhibits a pronounced "beating" amplitude envelope paced by eccentricity).

### Q4: How does the simulated data line up with what we have said is the repeat interval for the orbital cycles?

• Answer: The periodograms match the theoretical Milankovitch timescales closely:
	• Eccentricity: Peaks near 94.7 ka and 125.1 ka (which combine to form the classic ~100-kyr cycle), plus a longer ~390–405 ka cycle.
	• Obliquity: Sharp single peak right at 41.0 ka.
	• Precession: Split doublet with peaks at 23.7 ka, 22.4 ka, and 19.0 ka (matching the ~19–23 kyr band).

### Q5: Our data also showed a period at 390.1 ka for eccentricity. Why did our figure above not show that?

• Answer: The horizontal axis of the periodogram plot was zoomed in to xlim(10, 150) (10 to 150 thousand years), so the 390.1-ka peak (the ~405-ka long eccentricity cycle) lies off-screen to the right.

### Q6: Are you surprised by how small (or large) these percentage changes are?

• Answer: (Open-ended reflection; look for engagement with magnitude.) Most students are surprised by how small the variations are—integrated summer solar energy at 65°N varies by only -1.6% to +1.7% around its 6.76 GJ/m² mean. This highlights that orbital variations are a gentle pacemaker rather than a massive direct energy switch, meaning internal climate feedbacks must amplify these small nudges into full glacial-interglacial cycles.

### Q7 (Unnumbered Q #1 after Q6): Look at your periodogram and printed period(s) for 65°N insolation. Where did Precession (~23 ka) and Eccentricity (~100 ka) go?

• Answer:
	• Why Precession (~23 ka) disappears: This dataset represents integrated summer insolation (total solar energy accumulated over the summer melt season, in GJ/m²). By Kepler's second law, when precession places Northern Hemisphere summer near perihelion (closest to the Sun), sunlight is more intense but Earth moves faster along its orbit, making summer shorter. Near aphelion, sunlight is weaker but Earth moves more slowly, making summer longer. Intensity and duration nearly cancel out when integrated over the season, leaving 41.1 ka (obliquity) as the sole dominant peak.
	• Why Eccentricity (~100 ka) is absent: Direct changes in annual/seasonal solar energy from eccentricity are tiny (<0.1%); eccentricity mainly modulates the amplitude of precession rather than supplying direct 100-ka energy.

### Q8 (Unnumbered Q #2 after Q6): Why might summer insolation near 65°N matter for whether winter snow survives to the following year?

• Answer: High northern latitudes (~65°N) contain vast continental landmasses (North America and Eurasia) capable of supporting massive ice sheets. Ice sheets grow not because winters get colder, but because summers are cool enough that winter snow fails to melt completely, allowing snow and ice to accumulate year after year (increasing surface albedo and triggering positive ice-albedo feedback).

## Part 3 — What do paleoclimate records tell us?


### Q9 (CO₂ Time Series): Does CO₂ stay constant through the last several glacial cycles? How many major cycles can you see?

• Answer:
	• No, atmospheric CO₂ fluctuates dramatically between roughly ~180 ppm during cold glacial maxima and ~280–300 ppm during warm interglacials.
	• Students can count ~7 to 8 major sawtooth cycles across the 800-kyr record (with interglacial peaks around ~0, ~125, ~240, ~335, ~405, ~610, ~690, and ~785 ka), indicating an average spacing of ~100 kyr.

### Q10 (Interpreting the Antarctic CO₂ Periodogram):

1. Identify the dominant cycle:
	• Answer: The strongest period is ~98–100 ka (98.1 ka in the printout). Smaller secondary peaks also appear right at obliquity (~40.7 ka) and precession (~23.6 ka). (Note: Minor shoulders around ~72 ka and ~118 ka are spectral leakage side-lobes from the finite 800-ka window and irregular cycle durations.)
2. Compare forcing vs. response:
	• Answer: Even though 65°N integrated summer insolation is dominated by 41 ka and has almost no direct power at 100 ka, atmospheric CO₂ and ice volume oscillate at ~100 ka because internal Earth-system feedbacks amplify and pace the response. Massive Late Pleistocene ice sheets survive moderate 41-ka obliquity warming peaks ("skipping" 1–2 obliquity beats) and take ~80–120 ka to grow unstable, while Southern Ocean circulation, sea-ice expansion, and deep-ocean carbon storage lock away and release CO₂ in sync with these longer glacial cycles.

### Q11 (LR04 Introduction): How far back does the LR04 record extend? Why is a long record useful for investigating whether ice-age rhythms changed?

• Answer:
	• The LR04 stack extends back ~5,320 ka (~5.3 million years)—more than 6.5 times longer than the 800-ka ice-core record.
	• An 800-ka record only captures ~8 cycles of a 100-ka rhythm, which is too short to see whether that rhythm has always existed. A 5.3-million-year record allows us to test whether Earth's climate paced itself differently earlier in geologic history under the same orbital forcing.

### Q12 (Interpreting the 5-Million-Year Benthic δ¹⁸O Record):

1. Long-term climate trend:
	• Answer: Moving forward in time (left to right, from 5,000 ka to 0 ka), baseline δ¹⁸O increases from ~3.0 ‰ in the Pliocene to ~4.2–4.5 ‰ in the Late Pleistocene. Higher benthic δ¹⁸O indicates long-term global cooling and the growth of large Northern Hemisphere ice sheets.
2. Amplitude of ice-age swings:
	• Answer: The peak-to-trough amplitude grows progressively larger over time: small ~0.3–0.5 ‰ fluctuations in the Pliocene (green), moderate ~0.8–1.0 ‰ swings in the Early Pleistocene (orange), and massive ~1.5–1.8 ‰ glacial-interglacial swings in the Late Pleistocene (blue).
3. Rhythm and spacing:
	• Answer: The Early Pleistocene (orange) has tightly packed, rapid, symmetric oscillations (~41-kyr spacing), whereas the Late Pleistocene (blue) shifts to wider, slower, sawtooth-shaped cycles (~100-kyr spacing).

### Q13 (Putting It All Together — MPT Cell):

1. Forcing vs. Response:
	• Answer: Incoming summer insolation (j_65north.csv) is dominated by 41 ka and has virtually no power at 100 ka, nor did orbital cycles change across the Mid-Pleistocene Transition. Therefore, insolation alone acts only as a trigger/pacemaker; internal feedbacks (ice-sheet thickness/albedo, bedrock regolith erosion, ocean circulation, and CO₂ greenhouse amplification) are required to explain the 100-ka ice ages of the last 800,000 years.
2. Signal Processing Takeaway:
	• Answer: In a raw time series, overlapping cycles and climate noise make it hard to objectively measure dominant timescales or prove when a regime shift occurred. Periodograms decompose the variance by period, cleanly revealing the dominant peak shifting from 41.1 ka (Early Pleistocene) to 98.1 ka (Late Pleistocene).

## Part 4 — Putting the evidence together

1. What changed about glacial–interglacial variability across the MPT? Cite evidence from at least two intervals.
	• Answer: Across the Mid-Pleistocene Transition (~1,250–700 ka), glacial cycles shifted in periodicity, amplitude, and shape:
		• Early Pleistocene (1,200–2,580 ka): Cycles were shorter (41.1 ka dominant period), smaller in amplitude (~0.8–1.0 ‰ in δ¹⁸O), and relatively symmetric.
		• Late Pleistocene (0–800 ka): Cycles lengthened to ~100 ka (98.1 ka dominant period), nearly doubled in amplitude (~1.5–1.8 ‰ in δ¹⁸O, ~100 ppm swings in CO₂), and became strongly asymmetric ("sawtooth": slow ~80–90 ka cooling/ice buildup followed by rapid ~10 ka deglaciation).
2. Which orbital timescale is closest to the dominant rhythm of the older cycles? Which is closest to the later cycles?
	• Answer:
		• Older cycles (Early Pleistocene): Obliquity (~41 kyr).
		• Later cycles (Late Pleistocene): Short Eccentricity (~100 kyr).
3. Why is it not enough to say "eccentricity caused the 100-kyr ice ages"? Consider ice sheets, CO₂, ocean circulation, and other feedbacks.
	• Answer: Direct insolation forcing from 100-kyr eccentricity is negligible (and absent from the 65°N integrated summer insolation spectrum), plus orbital forcing did not change across the MPT when the 100-kyr cycles began. Instead, the 100-kyr rhythm emerges from internal feedbacks: thicker ice sheets (enabled by long-term cooling and erosion of slippery regolith down to hard bedrock) survive moderate 41-ka obliquity warming peaks ("skipping beats" for 2–3 obliquity cycles), while Southern Ocean sea-ice expansion and deep-ocean carbon storage draw down atmospheric CO₂ during glacials and release it rapidly during terminations, paced indirectly by eccentricity's modulation of precession.
4. What is one limitation of using a periodogram to explain past climate?
	• Answer: Any of the following valid points:
		• Correlation ≠ causation: A spectral peak shows recurring periodicity, not the physical mechanism driving it.
		• Stationarity assumption: A standard periodogram averages power across the entire time window, hiding when a cycle starts, stops, or shifts (which is why we had to split the LR04 record manually before and after the MPT).
		• Loss of phase/shape information: Periodograms discard timing (phase) and asymmetry, so they cannot show the sawtooth shape of rapid deglaciations vs. slow glaciations.
		• Windowing/resolution artifacts: Finite record lengths and uneven sampling require interpolation and can create spectral leakage or side-lobes.
