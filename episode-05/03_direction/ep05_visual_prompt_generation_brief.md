# EP05 VISUAL PROMPT GENERATION BRIEF
> This file is a session handoff document. Copy-paste this as the opening prompt in a new Claude Code session.
> After pasting, Claude will read all mandatory files and generate `ep05_visual_prompts_v01.md`.

---

## PROMPT (Copy-paste below into new session)

---

Generate visual prompts for EP05.

Bu oturum sadece visual prompt generation icin. Dramaturji onaylandi. Asagidaki kritik bilgileri oku ve uygula:

### MANDATORY READS (Standard Pipeline)
Sirasyla oku:
1. `_management/master.md`
2. `_management/pipeline_rules.md`
3. `_memory/lessons.md` — OZELLIKLE: "amber eyes" kurali, 16:9 kurali, short identifier kurali, reference image kurallari
4. `_assets/cast/character_profiles.json` — Robochica tasarimi GUNCELLENDI, oku
5. `episode-05/03_direction/ep05_dramaturgy_v01.md` — ONAYLANDI, 32 sahne
6. `episode-05/03_direction/ep05_concept_notes.md` — 8 human override, 12 creative rule
7. `_skills/robotiko-visual-prompts/SKILL.md` — Skill kurallari
8. `_templates/visual_prompt_template.md` — Output formati

### EP05 OZET BILGI (Hizli Referans)

**Bolum:** EP05 — "First Love / Blue Screen"
**Sahne sayisi:** 32 (dramaturji onaylandi 2026-03-31)
**Phase:** Phase 2: Destruction
**BPM:** 122 | **Key:** E Minor | **Sure:** 4:27 (267s)
**Ton:** Komedi → Trajedi. 3:24'e kadar saf komedi, sonra mask drop.

### KARAKTERLER

**Robotiko (Phase 2):**
- `visual_prompt_addition`: "rusted and cracked chrome chassis, sparks flying from joints, glitching blue-red eyes, exposed and fraying analog wires, battle-damaged retro-futuristic body"
- ref: `_assets/cast/ref_robotiko_master.png`
- Short identifier (ref image ile): "the chrome android"
- BU BOLUMDE: Davranisi vucuduna zit — asik, hevesli, enerjik. Hasar heyecan olarak okunuyor (Act 1-2), sistem arizasi olarak (Act 3).

**Robochica (YENİ KARAKTER):**
- `base_visual_prompt`: "Retro-futuristic chrome female android, 70s sci-fi feminine form — elegant curves in chrome plating, distinct from Robotiko but clearly from the same aesthetic universe. Exposed warm-toned analog wires (gold and copper), glowing amber-gold eyes (steady, warm), subtle scratches and minor wear marks on chrome (NOT pristine, carries her own history). Art deco-influenced head shape, slightly more elongated than Robotiko. One unique visual signature: a fractal/mandala pattern etched into her left shoulder plate, identifiable even in silhouette."
- ref: `_assets/cast/ref_robochica_master.png` (HENUZ URETILMEDI — reference prompt yazilmali)
- **AMBER EYES KURALI:** lessons.md'deki kurala gore "amber eyes" yazma! "warm amber-gold glow radiating softly around her eyes" veya "soft golden light emanating from her gaze" yaz. Gozleri literal amber rengi yapma — cevresinde sicak amber aura olsun.
- **MIRROR PRENSIBI:** Max 3 face-on sahne. Diger sahnelerde profil, siluet, yansima, partial view.
- Short identifier (ref image ile): "the chrome female android with warm gold wires and fractal shoulder pattern"

**Mentor:** BU BOLUMDE FIZIKSEL OLARAK YOK. Hicbir sahnede goruntulenmeyecek. Amber renk yankilari ortam isiklendirmesinde ve Robochica'nin gozlerinde zaten mevcut.

**Yasli Robot Cift (S11 — Hayal Karakterleri):**
- Sadece S11'de. Dreamlike/soft-focus islem.
- Yasli Erkek Robot: yipranmis chrome, patina, baston
- Yasli Kadin Robot: yipranmis chrome, "electric vibe" enerji kalkani/aura
- Reference prompt gerekli (yeni karakterler)

### REFERENCE IMAGE IHTIYACLARI (Step 0)

Sahne promptlarindan ONCE su reference promptlari yaz:

1. **REF-CHAR-01: Robochica** — Full figure, front-facing, well-lit. Tam visual prompt addition. 16:9. Suffix ile.
2. **REF-CHAR-02: Elderly Robot Couple** — Iki yasli robot yan yana. Dreamlike treatment notu. 16:9. Suffix ile.
3. **REF-ENV-01: Retro-Futuristic Supermarket** — Chrome raflar, analog fiyat gostergeleri, amber tavan isikleri, 70s urunler. No characters. Wide establishing shot. 16:9. Suffix ile.
4. **REF-ENV-02: Retro-Futuristic Street** — Chrome-beton kaldırim, analog sokak lambalari (amber), buhar cikan izgaralar. No characters. 16:9. Suffix ile.
5. **REF-ENV-03: Retro-Futuristic Cafe/Canteen** — Chrome tezgah, analog kadranlar, yuvarlak tabureler, amber sarkit lambalar, mekanik kahve makinesi. No characters. 16:9. Suffix ile.
6. **REF-ENV-04: Retro-Futuristic Office** — Chrome masalar, analog CRT terminaller, mekanik klavyeler, vakum tup aydinlatma. No characters. 16:9. Suffix ile.
7. **REF-ENV-05: Industrial Cathedral (Solo Space)** — Devasa demir-chrome kemeri duvarlar, kirik tavan camlari, amber isik huzmeleri, cilali chrome zemin. Surreal, melankoli. No characters. 16:9. Suffix ile.
8. **REF-ENV-06: Robotiko's Room** — Kucuk retro-futuristik oda, chrome duvarlar, tek CRT terminal, analog saat, dar karyola, amber masa lambasi. No characters. 16:9. Suffix ile.

### 8 HUMAN OVERRIDE — GORSEL DETAYLARI

Bu 8 override non-negotiable. Her biri dramaturjide detayli aciklandi ama su ozel gorsel detaylara dikkat:

1. **S05 (Both in Frame):** Robochica yuruyor, Robotiko izliyor. IKISI AYNI KAREDE.
2. **S07 (Drool):** Robotiko'nun agzindan yag/sivi damlıyor. KOMIK, igrendirici degil. Amber isikta guzelce parlasin.
3. **S11 (Elderly Couple):** Ekrana GERCEKTEN yasli robot cift geliyor. Dreamlike filter. Baston kaldiran yasli adam + enerji kalkani gosteren yasli kadin.
4. **S13 (robochica_1 Tattoo):** "robochica_1" yazisi OKUNAKLI olmali. Amber cizgiler chrome uzerinde. "_1" subscript net gorunmeli — EP06 payoff icin kritik.
5. **S15 (Hacker Mask + Physical Cloud):** IKI COMPOSITION: (A) Chrome mesh hacker maskeli Robotiko close-up. (B) Masada oturuyor, fiziksel ip yukari gidiyor, ucunda LITERAL MAVI BULUT, ustunde VERI MERKEZI BINASI. Ipi kesiyor. Start-End Keyframe onerildi.
6. **S22-S23 (Windows Folders):** WINDOWS KLASOR IKONU fiziksel olarak elinde. Sari klasor. Sonra FIRLATIYOR, kagitlar ucusuyor.
7. **S24 (Bright Red Body):** Tum vucut KIPKIRMIZI. Overheating. Elektrik arklari. Dramatik renk degisimi.
8. **S28 (Eye Projection):** Gozlerinden Robochica'nin goruntusü PROJEKSIYON olarak cikiyor. EP03 cinci hoca sahnesi gibi. Sicak projeksiyon, soguk oda.

### OZEL SAHNELER

**S19 (Inner Light / Kintsugi Preview):** Almost-Touch DEGIL. Robotiko'nun gogus catlaklarindan BIRKAC INCE amber isik huzmesi siziyor. Abartisiz, sessiz, birkac isik huzmesi. EP09 Kintsugi'nin bilincsiz habercisi.

**S20 (Album Cover Shot):** Bolumun POSTER KARESI. Wide shot, iki figur, devasa mekan, prog rock album kapagi kalitesinde olmali. Frank Frazetta mitik enerji + robot ask.

**S30 (Blue Screen):** Kodachrome tamamen drene olmus. Soguk, derin, varolussel mavi. Windows BSOD DEGIL. robochica_1 dovmesi soguk mavi isikta yara gibi gorunuyor.

### RENK PALETI KURALLARI

- **Act 1-2 (S01-S25):** Sicak Kodachrome, amber sokak lambalari, gold tonlar. SIFIR karanlik/soguk ipucu.
- **Act 3 (S26-S32):** Soguk dijital mavi. Kodachrome drene oluyor. Amber TAMAMEN yok.
- **Gecis noktasi:** S26-S27 hafif soguma, S28'den itibaren tam Blue Screen.
- **Amber = yanlis yorumlanmis hakikat.** Her yerde var ama romantik baglamda (Robochica'nin gozleri, sokak isiklari, dovme isigi).

### TEKNIK HATIRLATMALAR

- Her promptta `16:9 widescreen composition` belirt
- Her prompt mandatory suffix ile bitmeli — ISTISNASIZ
- Karakter isimleri YAZMA (Robotiko, Robochica, Mentor) — gorsel tanim kullan
- Reference image varsa SHORT IDENTIFIER kullan, uzun aciklama tekrarlama
- Kamera hareketi YAZMA — o motion script'in isi
- Negatif prompt YAZMA — ne OLDUGUNU yaz, ne OLMADIGINI degil
- S15 icin Start-End Keyframe: S15a (maskeli yuz) ve S15b (ip kesiyor) olarak iki prompt yaz
- Forbidden aesthetics: clean/sterile/Pixar/neon cyberpunk/smooth plastic

### CIKTI

`episode-05/04_visuals/ep05_visual_prompts_v01.md` dosyasina yaz.
8 reference prompt + 33 sahne promptu (32 sahne + S15 icin 2 keyframe = 33) = toplam ~41 prompt.

Dramaturji dosyasindaki her sahneyi sirasi ile isle. Her sahnenin timestamp, dramaturgy reference, characters, ref path, video tech strategy, composition notes ve text prompt alanlari olmali.

Sonunda post-generation checklist ile dogrula.

---

*Bu brief'i yeni sohbete kopyala-yapistir. Claude tum dosyalari okuyup visual promptlari uretecek.*
