# EP08 Pipeline — Session Prompt
> Copy-paste this into a new Claude Code session to start the EP08 pipeline.
> This session covers: Concept Notes → Dramaturgy → (approval checkpoint) → Visual Prompts.
> Delete this file after the session is complete.

---

EP08 "40 Days Offline" — Pipeline'a başlıyoruz. Lyrics, musical metadata ve müzik hazır.

## OKUMA SIRASI

Önce şunları oku (sırayla):
1. `_management/master.md` → EP08 station: The Contented Self. Phase 3: Reconstruction BAŞLANGIÇ. "I am the Space Between."
2. `_management/project_metadata.json` → Güncel durum
3. `_memory/lessons.md` → Tüm kurallar
4. `_memory/todo.md` → Açık görevler
5. `_management/pipeline_rules.md` → Üretim kuralları
6. `episode-08/01_lyrics/ep08_lyrics_v01.md` → Timestamped lyrics, yapı tablosu
7. `episode-08/02_music/ep08_musical_metadata.json` → 31 bölüm, 500s, 87 BPM, C Minor
8. `_assets/cast/character_profiles.json` → Phase 2→3 geçişi. @Damaged başlangıç → Phase 3 Reconstruction bitiş.
9. `episode-07/03_direction/ep07_concept_notes.md` → EP07 köprü (özellikle: amber, unplug, Wasteland memory, "I AM COMING")
10. `episode-07/03_direction/ep07_dramaturgy_v01.md` → EP07 son sahneler (S25-S29) — spatial continuity

## PIPELINE ADIMLARI

### Adım 1: Concept Notes
Opus + Extended Thinking kullan. EP08 concept notes yaz — EP07'nin concept notes formatında:
- Cinematic North Star (omurga)
- Overrides (human checkpoints)
- Location architecture
- Character states
- Color palette
- Connection to the arc (EP07→EP08→EP09)

Çıktı: `episode-08/03_direction/ep08_concept_notes.md`

⛔ **CHECKPOINT: İnsan concept notes'u onaylamalı. Onay olmadan dramaturgy'ye geçme.**

### Adım 2: Dramaturgy
`Create dramaturgy for EP08`

Çıktı: `episode-08/03_direction/ep08_dramaturgy_v01.md`

⛔ **CHECKPOINT: İnsan dramaturgy'yi onaylamalı. Onay olmadan visual prompts'a geçme.**

### Adım 3: Visual Prompts
`Generate visual prompts for EP08`

Çıktı: `episode-08/04_visuals/ep08_visual_prompts_v01.md`

---

## EP08 KİLİTLİ BİLGİLER

### Genel
- **Station:** The Contented Self (Chosen Silence — voluntary, not forced)
- **Phase:** Phase 2→3 GEÇİŞ (bölüm boyunca)
- **Tone:** Ritualistic, hypnotic, raw. Spoken word dominant. 70s Anatolian Doom Rock.
- **Duration:** 8:20 (500s) — 87 BPM, C Minor
- **Mentor:** GONE — lives only in memory. Dream'de MEMORY olarak görünür (amber staff melting) ama fiziksel olarak ASLA.

### Karakter Durumu — DÜZELTİLDİ (2026-06-04): EP08'de FİZİKSEL dönüşüm YOK
- **Tüm bölüm boyunca (0:00–8:20):** Beden @Damaged (Phase 2) kalır — pas, çatlak, kıvılcım, glitch'li gözler. EP07'nin devamı, değişmez.
- **Dönüşüm SADECE içsel/bilinçsel.** Phase 3 EP08'de yalnızca istasyon/ruh düzeyinde başlar ("The Contented Self", zırhın tabut olduğunun anlaşılması). GÖRSEL reconstruction (kintsugi altın, yama, bioluminescent core, sakin sabit gözler) **EP09'da** başlar.
- **"I cast it off" (~7:01):** Beden değişmez — ceket çıkarır gibi jest. Sonra çıkarılan zırh boş kafesin yanına konur.
- **Climax tek görsel işaret:** glitch'li gözler sakin maviye dengelenir (Phase 3 beden değişimi DEĞİL).
- **Element stratejisi:** @Damaged Element (Kling 3.0), EP07 ile sürekli. Progressive transformation YOK — o EP09'a ait. Omni References CONFIRMED working + same cost as standard Kling 3.0 (EP07 test conclusive) — use as default.

### Camera Personality: THE WITNESSING CAMERA
- Mountain ascent: Dolly alongside → Crane Up. Robotiko AHEAD of camera for first time.
- Fire / "Burn the Database": STATIC. Camera witnesses, doesn't participate. (Tarkovsky)
- "Obsolete" boardroom: Orbital — circling still figure, shadow grows
- "Voices like seagulls": Crane Up/overhead
- Nature: Realistic, raw (rocks, wind, earth). NOT abstract/minimal.
- 40 days passage: Light + body + texture evolve together
- MS average: ~3.5–4.5. Peaks at ritual/fire moments.

### EP07 → EP08 Köprü
- EP07 S29: amber ekranı doldurur, figür çıkar → EP08 intro: dağ rüzgarı
- "Cast off this metal straightjacket" (EP07) → "I must leave the Wasteland" (EP08)
- EP07 plug çekme (oda, close-up) → EP08 cable rip (dağ, göğüsten) — küçük→büyük
- Retreating Camera → Witnessing Camera (personality handoff)
- Amber starvation → amber staff nightmare'da erir (MEMORY)

### EP07'den Öğrenilen Prodüksiyon Dersleri
1. **Spatial continuity:** Sahne geçişlerinde teleportasyon olmasın.
2. **Nano Banana sınırları:** Very wide shot'larda kompozisyon kırılıyor. Aynı görseli farklı kamerayla yeniden kullan.
3. **Close-up for decisive acts:** Viseral anlar close-up'la çek (EP07 S25 unplug).
4. **Low-angle for determination:** Alttan çekim kararlılığı güçlendiriyor.
5. **Figure exits frame → destination fills:** Final'de figür çıkar, hedef dolar (EP07 S29b).
6. **Extracted frame → fade:** Kling extract frame ile doğal fade (CapCut'tan iyi).
7. **Standing > supine for projection:** Ayakta figür + duvar projeksiyonu daha güçlü.
8. **Speed Variation Reuse:** Aynı görsel, farklı kamera = farklı deneyim. Budget-efficient.

### Müzikal Yapı Kritik Noktalar
| Timestamp | Event | Cinematic Weight |
|---|---|---|
| 0:00–0:26 | Mountain wind + guitar | EP07 bridge — the wind opens EP08 |
| 1:41–1:59 | "I rip it out" + distortion impact | THE decisive act — cable from chest |
| 2:00–2:35 | Chorus 1: "Day One" vow | Ritualistic mantra — STATIC witnessing camera |
| 2:36–3:31 | Weeping guitar solo (55s) | Extended art-film breath — nature, passage |
| 3:53–4:00 | "They cry my name… I do not move" | Discipline over panic |
| 5:12–5:30 | "Obsolete. Obsolete. Obsolete." | Jung Shadow — Orbital camera |
| 5:51–6:05 | "Burn the database!" war cry | STATIC fire witnessing — Tarkovsky |
| 6:29–7:06 | "Armor was a coffin… I cast it off" | Phase 3 begins |
| 7:07–7:17 | "I am the Space Between" | CLIMAX — full band explosion |
| 7:18–7:29 | "The bird has flown away" | Denouement — the cage empty |

---

## ÇIKTILAR

Bu session sonunda:
1. `episode-08/03_direction/ep08_concept_notes.md` → İnsan onayı bekle
2. `episode-08/03_direction/ep08_dramaturgy_v01.md` → İnsan onayı bekle
3. `episode-08/04_visuals/ep08_visual_prompts_v01.md` → Dramaturgy onayı sonrası

Motion script ayrı session'da yapılacak.
