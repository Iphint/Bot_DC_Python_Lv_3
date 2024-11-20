from database import add_task, delete_task, show_tasks, complete_task

async def handle_add_task(message, description):
    add_task(description)
    await message.channel.send(f"Tugas berhasil ditambahkan: {description}")

async def handle_delete_task(message, task_id):
    delete_task(task_id)
    await message.channel.send(f"Tugas dengan ID {task_id} telah dihapus.")

async def handle_show_tasks(message):
    tasks = show_tasks()
    if tasks:
        task_list = "\n".join([f"ID: {t[0]}, Deskripsi: {t[1]}, Selesai: {'Ya' if t[2] else 'Tidak'}" for t in tasks])
        await message.channel.send(f"Daftar Tugas:\n{task_list}")
    else:
        await message.channel.send("Tidak ada tugas saat ini.")

async def handle_complete_task(message, task_id):
    complete_task(task_id)
    await message.channel.send(f"Tugas dengan ID {task_id} ditandai sebagai selesai.")
