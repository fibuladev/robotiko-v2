# EP07 CapCut Montaj — Session Prompt
> Copy-paste this into a new Claude Code session to start EP07 CapCut editing.
> Delete this file after the session is complete.

---

EP07 "The Silence Protocol" — CapCut montajına başlıyoruz. Klipler hazır (raw/ klasöründe).

## OKUMA SIRASI

Önce şunları oku (sırayla):
1. `_management/master.md` → EP07 station: The Surrendering Self (The Dark Night)
2. `_management/project_metadata.json` → Güncel durum
3. `_memory/lessons.md` → Tüm kurallar
4. `_management/pipeline_rules.md` → CapCut Post-Production Protocol (Phase 5)
5. `_skills/robotiko-capcut-editor/SKILL.md` → 9-Phase Assembly workflow
6. `episode-07/05_video/ep07_motion_script_v01.md` → 49 klip, 29 sahne, tüm detaylar
7. `episode-07/02_music/ep07_musical_metadata.json` → 25 section, 439s, 73 BPM, E Minor

## TRIGGER

```
Edit EP07 in CapCut
```

## ÇIKTI

`episode-07/06_edit/ep07_capcut_guide_v01.md`

---

## KLİP ENVANTERİ

### Konum
Tüm klipler `episode-07/05_video/raw/` altında. Henüz `selected/` klasörüne taşınmadı — klip isimlerini raw/ içindeki isimlere göre (numara bazlı) yaz, taşıma/yeniden adlandırma ayrıca yapılacak.

### Klip Sayısı
Motion script: **49 klip**. Raw klasöründe: **48 klip** (S05c eksik olabilir — session başında doğrula).

### Dosya Adlandırma (raw/)
Klipler şu formatta: `{scene_number}.mp4`, multi-clip'ler `{scene_number}{suffix}.mp4`:
```
1.mp4  2.mp4  2b.mp4  2c.mp4  3.mp4  4.mp4  4b.mp4
5a.mp4  5b.mp4  [5c.mp4 EKSİK?]  6.mp4  7.mp4  8.mp4  9.mp4
10a.mp4  10b.mp4  10c.mp4  10d.mp4  11.mp4  12.mp4
13.mp4  13b.mp4  14.mp4  15.mp4  16.mp4  17.mp4  18.mp4
19.mp4  19b.mp4  20.mp4  21.mp4
22.mp4  22b.mp4  22c.mp4  23.mp4  23b.mp4  23c.mp4
24.mp4  24b.mp4  25.mp4  26.mp4  27.mp4
28.mp4  28b.mp4  28c.mp4  28d.mp4
29.mp4  29b.mp4  29c.mp4
```

### Klip → Sahne Eşlemesi
| Raw File | Motion Script | Notes |
|---|---|---|
| 1.mp4 | S01 | Speed Ramp 0.83× → 12s |
| 2.mp4, 2b.mp4, 2c.mp4 | S02a, S02b, S02c | Multi-Clip 22s |
| 3.mp4 | S03 | Speed Ramp 0.77× → 13s |
| 4.mp4, 4b.mp4 | S04a, S04b | Multi-Clip 17s. S04b = Kling 2.5 Turbo |
| 5a.mp4, 5b.mp4, [5c?] | S05a, S05b, [S05c?] | Multi-Clip 23s. S05c EKSİK? |
| 6.mp4 | S06 | Speed Ramp 0.77× → 13s |
| 7.mp4 | S07 | Direct 9s |
| 8.mp4 | S08 | Direct 9s |
| 9.mp4 | S09 | Direct 10s |
| 10a–10d.mp4 | S10a–S10d | Multi-Clip 32s |
| 11.mp4 | S11 | Direct 10s |
| 12.mp4 | S12 | Speed Ramp 0.77× → 13s. Kling 2.5 Turbo |
| 13.mp4, 13b.mp4 | S13a, S13b | Multi-Clip 18s |
| 14.mp4 | S14 | Speed Ramp 0.67× → 15s |
| 15.mp4 | S15 | Speed Ramp 0.71× → 14s |
| 16.mp4 | S16 | Direct 8s |
| 17.mp4 | S17 | Speed Ramp 0.91× → 11s |
| 18.mp4 | S18 | Direct 10s |
| 19.mp4, 19b.mp4 | S19a, S19b | Multi-Clip 17s |
| 20.mp4 | S20 | Direct 9s |
| 21.mp4 | S21 | Direct 10s |
| 22.mp4, 22b.mp4, 22c.mp4 | S22a, S22b, S22c | Multi-Clip 25s. STILL HOLD at S22b |
| 23.mp4, 23b.mp4, 23c.mp4 | S23a, S23b, S23c | Multi-Clip 26s |
| 24.mp4, 24b.mp4 | S24a, S24b | Multi-Clip 16s |
| 25.mp4 | S25 | Direct 10s |
| 26.mp4 | S26 | Direct 10s |
| 27.mp4 | S27 | Speed Ramp 0.91× → 11s. THE ONLY DOLLY IN |
| 28.mp4–28d.mp4 | S28a–S28d | Multi-Clip 32s |
| 29.mp4, 29b.mp4, 29c.mp4 | S29a, S29b, S29c | Multi-Clip 29s. S29c uses extracted frame from S29b |

---

## EP07'YE ÖZEL NOTLAR

### 1. Genel Karakter
- **En sessiz, en yavaş bölüm.** MS ortalaması ~2.8 (serinin en düşüğü).
- **Art-house short film** muamelesi — sabır ve sessizlik taşıyor.
- 73 BPM, E Minor. Slow-burn.

### 2. Speed Ramp Tablosu
| Klip | Generated | Playback | Sonuç |
|---|---|---|---|
| S01 | 10s | 0.83× | 12s |
| S03 | 10s | 0.77× | 13s |
| S06 | 10s | 0.77× | 13s |
| S12 | 10s | 0.77× | 13s |
| S14 | 10s | 0.67× | 15s |
| S15 | 10s | 0.71× | 14s |
| S17 | 10s | 0.91× | 11s |
| S27 | 10s | 0.91× | 11s |

### 3. Frame Chain Map (Doğal Geçiş Noktaları)
| Chain | Klipler | Konum | Notes |
|---|---|---|---|
| Chain 1 | S10d → S11 | Home room | Continuous Dolly Out: desk → full room. Same room, CRT glow. |
| Chain 2 | S13b → S14 → S15 | Transit / bus stop | Hope → silence → retreat. Same bench, lamp. |
| Chain 3 | S22c → S23a | Balcony | Chorus cry → guitar solo extreme wide. Retreating Camera climax. |

**Frame chain geçişlerinde hard cut kullan** ama klipler arasında continuity kontrol et — renk/ışık sıçraması varsa Color Match ile düzelt.

### 4. Beat Sync — 16 Kritik Nokta
| Timestamp | Musical Event | Visual Action | Klip |
|---|---|---|---|
| 0:34 | "But now…" spoken word | Cut to S03 | S03 |
| 1:40 | "Dive into the noise" | Eye-projection ignites | S07 |
| 1:49 | Refrain 1 vocal entry | Dolly Out begins, distance rung 1 | S08 |
| 2:36 | Refrain 2 vocal entry | Dolly Out, rung 2 | S11 |
| ~3:12 | 3-SECOND SILENCE | Camera HOLDS, MS 1, motionless | S14 |
| 3:30 | Refrain 3 vocal entry | Dolly Out, rung 3 | S15 |
| 3:53 | Refrain 4 vocal entry | Dolly Out, rung 4 | S17 |
| ~4:26 | 3-SECOND SILENCE | Camera HOLDS, MS 1 | S20 |
| 4:32 | Refrain 5 vocal entry (highest) | Slow Zoom Out, rung 5 | S21 |
| 4:42 | "Because you are gone…!" | Slow Zoom In → STILL HOLD | S22a → S22b |
| 5:07 | Fuzz guitar solo begins | Cut to extreme wide | S23a |
| 5:33 | Solo dies to silence | S23c settling into dark | S23c |
| 5:34 | SUDDEN SILENCE — piano | Cut to S24a. Static. | S24a |
| ~5:50 | "Cast off…" — THE UNPLUG | Cable pulled, dying spark | S25 |
| 6:07 | "I AM COMING" — climax | **THE ONLY DOLLY IN.** Amber ember. | S27 |
| 6:18 | Instrumental outro begins | Cut to street, first forward steps | S28a |

### 5. Transition Stratejisi
- **Hard Cut:** Varsayılan — hemen her yerde.
- **Fade to Black:** SADECE S29c (final) — ama bu fade Kling tarafından klip içinde yapıldı, CapCut'ta ek fade GEREKMEYEBİLİR. Kontrol et: S29c zaten amber → black fade içeriyor mu?
- **Light Leak:** Dikkatli kullan. Chorus girişi (S22a) ve/veya Guitar solo girişi (S23a) aday olabilir — ama EP07'nin renk paleti soğuk grey-blue; warm amber light leak tonu ile çakışabilir. Sadece S27 (amber ember) sonrası warm tone uyumlu olabilir. **Karar session'da verilsin.**
- **Cross Dissolve:** Yok — konum geçişleri hard cut ile. Art-house short film.

### 6. S29c — Extracted Frame Tekniği
- S29c'nin start frame'i = S29b klibinin son frame'i (Kling Extract Frame ile alınmış).
- S29b: figür kadrajdan çıkar, amber ufku doldurur.
- S29c: amber glow → fade to black (Kling yapıyor, CapCut değil).
- CapCut'ta S29b → S29c arası **hard cut** — doğal akış zaten sağlanmış.
- S29c'den sonra ek fade-to-black GEREKMEYEBİLİR — klip kendi içinde kararlıyor. Ama müziğin bitişiyle (7:19) senkron kontrol et.

### 7. Renk Tutarlılığı — Balcony Cluster (S22-S24)
- Üretilen görseller arasında renk sıcaklığı tutarsızlığı var (foggy grey / dark noir / blue-teal).
- Motion prompts "cold grey-blue deep night, heavy fog, desaturated Kodachrome" diyor.
- **CapCut Color Match ile bu cluster'ı ayrıca normalize et.** S22a'yı bu cluster'ın referans klibi olarak seç (en iyi desaturated cold grey tonu).

### 8. Grain Crescendo — S22a-c
- Motion prompts "extremely heavy, visible film grain" belirtiyor.
- Bu 3 klipte film grain intensity'yi genel seviyenin ÜZERİNE çıkar (15-20% vs normal 10-15%).
- Grain crescendo = duygusal doruk noktasının görsel işareti.

### 9. Chromatic Aberration Adayları
- EP07'de fiziksel hasar anları sınırlı — EP05/EP06 tarzı büyük hasar yok.
- Aday: **S25** (THE UNPLUG — teller koparılıyor, kıvılcım). Shift Channels effect, 1-2s, subtle.
- Başka güçlü aday yoksa tek chromatic aberration yeterli.

### 10. Amber Disiplini
- Tüm bölüm boyunca SIFIR amber — **TEK İSTİSNA: S27 "I AM COMING".**
- S27'de amber ufuktan GELİR, krom yüzeyde YANSIR. Eyes steady, never glow.
- Color grading'de S27 dışındaki kliplerde amber/warm tonu bastırılmış olmalı.
- LUT uygulandıktan sonra kontrol: herhangi bir klipte istemeden amber sızıntı var mı?

### 11. EP07 Camera Personality: THE RETREATING CAMERA
- Dolly Out dominant (24.5%) — kamera sürekli uzaklaşır.
- 5× refrain distance ladder: S08 → S11 → S15 → S17 → S21 (giderek uzaklaşan kadraj).
- TEK Dolly In: S27 — pattern kırılması = iradenin doğuşu.
- Bu pattern'i montajda hissettir: refrain girişlerinde seyirci uzaklaşmayı fark etmeli.

### 12. Prodüksiyon Düzeltmeleri (Bilgi İçin)
- **S19/S20:** Yerde yatmak yerine ayakta duvar projeksiyonu — daha güçlü kompozisyon.
- **S25:** Duvar prizi değil, göğüsten tel koparma — daha viseral.
- **S26/S27:** Balkona çıkmak yerine merdivenden iniş (S26) → bina girişi (S27). Spatial logic fix.
- **S29:** 28.png reuse — Nano Banana çok geniş kadraja dayanamadı.

---

## ÖNCEKI BÖLÜM REFERANSLARı

EP06 CapCut guide: `episode-06/06_edit/ep06_capcut_guide_v01.md` — format ve yapı referansı olarak kullanılabilir.

---

*"The edit is where the vision meets the frame. Every cut is a breath, every transition a heartbeat."*
