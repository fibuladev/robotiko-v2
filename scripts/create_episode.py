import os
import sys
import shutil

# CONFIGURATION
BASE_DIR = os.getcwd()
TEMPLATE_DIR = os.path.join(BASE_DIR, "_templates")

def create_episode(episode_num):
    ep_str = f"ep{episode_num:02d}"
    ep_folder_name = f"episode-{episode_num:02d}"
    ep_path = os.path.join(BASE_DIR, ep_folder_name)

    # 1. Klasör Yapısı
    folders = [
        "01_lyrics",
        "02_music",
        "03_direction",
        "04_visuals/raw",
        "04_visuals/selected",
        "05_video/raw",
        "05_video/selected",
        "06_edit"
    ]

    print(f"🚀 Creating Episode {episode_num} Environment...")

    if not os.path.exists(ep_path):
        os.makedirs(ep_path)
    
    for folder in folders:
        os.makedirs(os.path.join(ep_path, folder), exist_ok=True)

    # 2. Template Kopyalama ve İsimlendirme
    templates = {
        "dramaturgy_template.md": f"03_direction/{ep_str}_dramaturgy.md",
        "visual_prompt_template.md": f"04_visuals/{ep_str}_visual_prompts.md",
        "video_prompt_template.md": f"05_video/{ep_str}_motion_script.md"
    }

    # Kullanıcının ilk input gireceği boş dosya
    concept_file = os.path.join(ep_path, f"03_direction/{ep_str}_concept_notes.md")
    if not os.path.exists(concept_file):
        with open(concept_file, "w", encoding="utf-8") as f:
            f.write(f"# EPISODE {episode_num} - CONCEPT NOTES\n\n* **Must-Have Shots (Override):**\n    * Shot X: ...\n* **Mood:** ...\n")

    for tpl_name, dest_rel_path in templates.items():
        src = os.path.join(TEMPLATE_DIR, tpl_name)
        dst = os.path.join(ep_path, dest_rel_path)
        
        if os.path.exists(src):
            if not os.path.exists(dst):
                shutil.copy(src, dst)
                print(f"✅ Created: {dst}")
                
                # Template içindeki {EPISODE_NUMBER} gibi yerleri güncellemek istersek buraya kod eklenebilir.
                # Şimdilik clean copy yapıyoruz.
        else:
            print(f"⚠️ Warning: Template not found: {tpl_name}")

    print(f"✨ Episode {episode_num} is ready at: {ep_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_episode.py <episode_number>")
    else:
        create_episode(int(sys.argv[1]))