from botcity.core import DesktopBot
from pynput.keyboard import Key, Controller 
import requests, os, time, json, urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Bot(DesktopBot):
    def action(self):
        self.keyboard = Controller()
        
        # 1. Setup Folder
        desktop = os.path.expanduser("~")
        folder = os.path.join(desktop, "Desktop", "tjm-project")
        if not os.path.exists(folder): os.makedirs(folder)

        # 2. Get Data
        posts = self.get_data()

        # 3. Process Posts
        for post in posts:
            post_id = post.get('id')
            print(f"--- Processing Post {post_id} ---")
            
            # Open Notepad
            if self.open_notepad():
                self.wait(2000) 
                
                # Write Content
                self.paste(f"Title: {post.get('title')}\n\n{post.get('body')}")
                
                # Save & Close
                self.save_file(post_id, folder)
            else:
                print("[ERROR] Skipped: Notepad icon not found.")
                
            self.wait(1000)

    def get_data(self):
        # --- COLLEAGUE'S CODE BLOCK (Adapted) ---
        try:
            # I used their exact request line (removed verify=False since they don't use it)
            response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=10)
            response.raise_for_status()
            
            print("[INFO] API Connected successfully!")
            # We must add [:10] because the API returns 100 posts, but you only want 10
            return response.json()[:10]
            
        except Exception as e:
            # If it fails, we print their error message
            print(f"[WARN] Error fetching posts: {e}")
        # ----------------------------------------

        # --- YOUR SAFETY NET (Keep this!) ---
        print("[WARN] Switching to local backup file.")
        
        # If the API above failed, we load from the file on your computer
        if os.path.exists("resources/posts.json"):
            with open("resources/posts.json", 'r', encoding='utf-8') as f:
                return json.load(f)[:10]
        
        return []

    def open_notepad(self):
        for i in range(3):
            # Check Light & Dark icons
            for icon in ["notepad_icon", "notepad_dark"]:
                if self.find(icon, matching=0.7, waiting_time=1500):
                    self.move()
                    self.click()
                    self.wait(200)
                    self.keyboard.press(Key.enter)
                    self.keyboard.release(Key.enter)
                    return True
            
            # Keep this so you know why it's waiting
            print(f"[INFO] Icon not found. Retrying... ({i+1}/3)")
            time.sleep(1)
        return False

    def save_file(self, post_id, folder):
        k = self.keyboard
        
        # 1. Ctrl + S
        with k.pressed(Key.ctrl): k.type('s')
        self.wait(2000)
        
        # 2. Type Path
        self.paste(os.path.join(folder, f"post_{post_id}.txt"))
        self.wait(1000)
        
        # 3. Enter
        k.press(Key.enter); k.release(Key.enter)
        self.wait(1500)
        
        # 4. Handle "Confirm Save As" (Silent)
        if self.find("confirm_save", matching=0.8, waiting_time=1000):
            
            # Press LEFT to select "Yes"
            k.press(Key.left); k.release(Key.left)
            self.wait(500)
            
            # Press ENTER to confirm "Yes"
            k.press(Key.enter); k.release(Key.enter)
            self.wait(500)

        # 5. Alt + F4
        with k.pressed(Key.alt): k.press(Key.f4)

if __name__ == '__main__':
    Bot().action()