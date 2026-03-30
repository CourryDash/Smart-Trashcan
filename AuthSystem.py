import datetime
import time

class AuthSystem:
    def __init__(self):
        self.petugas_ids = ["123"]
        self.admin_ids = ["999"]

        # PIN admin
        self.admin_pin = "4321"

        # Status sistem
        self.system_active = True

        # Keamanan
        self.failed_attempts = 0
        self.max_attempts = 3
        self.locked = False

        # Log aktivitas
        self.logs = []

    def login(self, user_id):

        # Cek sistem aktif atau tidak
        if not self.system_active:
            print("Sistem sedang nonaktif (maintenance).")

            time.sleep(1)

            return None

        # Jika terkunci
        if self.locked:
            if user_id in self.admin_ids:
                print("Admin mencoba membuka sistem...")

                time.sleep(1)

                if self._verify_admin_pin():
                    self.reset_system()
                    self._handle_success(user_id, "ADMIN (UNLOCK)")
                    return "admin"
                else:
                    self._handle_failed(user_id)
                    return None
            else:
                print("Sistem terkunci! Akses ditolak.")

                time.sleep(1)

                return None

        # Admin
        if user_id in self.admin_ids:
            if self._verify_admin_pin():
                self._handle_success(user_id, "ADMIN")
                return "admin"
            else:
                self._handle_failed(user_id)
                return None

        # Petugas
        elif user_id in self.petugas_ids:
            self._handle_success(user_id, "PETUGAS")
            return "petugas"

        # Gagal
        else:
            self._handle_failed(user_id)
            return None



    # VERIFIKASI PIN
    def _verify_admin_pin(self):
        pin = input("Masukkan PIN admin: ")
        if pin == self.admin_pin:
            return True
        else:
            time.sleep(1)
            print("PIN salah!")
            return False



    # HANDLER
    def _handle_success(self, user_id, role):
        self.failed_attempts = 0
        self.log_activity(user_id, f"BERHASIL ({role})")

    def _handle_failed(self, user_id):
        self.failed_attempts += 1
        self.log_activity(user_id, "GAGAL")
        print("Autentikasi gagal!")

        time.sleep(2)

        if self.failed_attempts >= self.max_attempts:
            self.locked = True
            self.trigger_alarm()



    # LOG ACTIVITY
    def log_activity(self, user_id, status):
        self.logs.append({
            "waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "id": user_id,
            "status": status
        })

    def logs_activity(self):
        return self.logs



    # CONTROL SYSTEM
    def shutdown_system(self):
        self.system_active = False
        print("Sistem dimatikan (maintenance mode).")
        time.sleep(1)

    def start_system(self):
        self.system_active = True
        print("Sistem dihidupkan kembali.")
        time.sleep(1)

    def reset_system(self):
        self.failed_attempts = 0
        self.locked = False

    def trigger_alarm(self):
        print("ALARM AKTIF!")
        print("Sistem dikunci karena percobaan ilegal!")

if __name__ == "__main__":
    auth = AuthSystem()

    while True:
        print("\n=== TEST SYSTEM ===")
        print("1. Scan Kartu")
        print("2. Lihat Log Aktivitas")
        print("3. Matikan Sistem")
        print("4. Hidupkan Sistem")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kartu = input("Scan kartu (ENTER untuk kembali): ")

            if kartu.strip() == "":
                print("Kembali...")

                time.sleep(1)
                
                continue

            role = auth.login(kartu)

            if role:
                print(f"Login berhasil sebagai: {role}")

                time.sleep(1)

            else:
                print("Login gagal")

        elif pilihan == "2":
            print("Melihat Log Aktivitas...")

            time.sleep(1)

            print("\n=== LOG AKTIVITAS ===")
            logs = auth.logs_activity()

            if not logs:
                print("Belum ada aktivitas.")

                time.sleep(1)

            else:
                for log in logs:
                    print(f"[{log['waktu']}] ID: {log['id']} | {log['status']}")

        elif pilihan == "3":
            if not auth.system_active:
                print("Sistem telah dinonaktifkan.")

                time.sleep(1)
            else:
                auth.shutdown_system()

        elif pilihan == "4":
            if auth.system_active:
                print("Sistem masih aktif.")

                time.sleep(1)

            else:
                auth.start_system()

        elif pilihan == "0":
            print("Keluar.")
            break

        else:
            print("Pilihan tidak valid!")