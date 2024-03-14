import os
import json

class MyTask:
    def __init__(self):
        self.id = 0       
             
    def create_task(self, user): 
        print('\n:::: Crear tarea ::::\n')
                
        try:
            nameTask = str(input('Nombre de la tarea: '))
            description = str(input('Descripción: '))
            completed = str(input('Completado: '))

            self.id += 1

            task = {'nombre': nameTask, 'descripcion': description, 'completado': completed, 'id': self.id}            

            all_tasks = [] 

            if os.path.exists(f'task_{user}.json') and os.path.getsize(f'task_{user}.json') > 0:
                with open(f'task_{user}.json', 'r') as file_json:
                    all_tasks = json.load(file_json)

            all_tasks.append(task)
            
            with open(f'task_{user}.json', 'w') as file_json:
                json.dump(all_tasks, file_json, indent=2)
                
            print('\nTarea creada con éxito.')
            
        except Exception as e:
            print(f'\nHubo un error: > {e}')
          
    def del_task(self, user):
        print('\n:::: Eliminar tareas ::::')
        try:
            file_path = f'task_{user}.json'
            if not os.path.exists(file_path):
                print('\nNo tienes tareas aún.')
                return

            with open(file_path, 'r') as file:
                task_data = json.load(file)

            if not task_data:
                print('\nNo tienes tareas aún.')
                return

            print('\nTareas:\n')
            for task in task_data:
                print(f"- {task['nombre']} | id: {task['id']}")

            confirm_delete = input('\n¿Estás seguro de que deseas eliminar una tarea? (si/no): ')

            if confirm_delete.lower() == 'si':
                id_task_to_delete = int(input('ID de la tarea a eliminar: '))

                updated_tasks = [task for task in task_data if task['id'] != id_task_to_delete]

                if len(updated_tasks) == len(task_data):
                    print(f"\nNo se encontró ninguna tarea con el ID '{id_task_to_delete}'.")
                else:
                    with open(file_path, 'w') as file:
                        json.dump(updated_tasks, file, indent=2)
                    print(f"\nLa tarea '{id_task_to_delete}' se ha eliminado con éxito.")
            else:
                print('\nNo se eliminó ninguna tarea.')

        except Exception as e:
            print(f'\nHubo un error: > {e}')
            
    def edit_task(self, user):
        print('\n:::: Editar tareas ::::')
        
        file_search = f'task_{user}.json'
        with open(file_search, 'r') as file:
            task_data = json.load(file) 
        
        if not task_data:
            print('\nNo tienes tareas aún.')
            return

        print('\nTareas:\n')
        for name in task_data:
            print(f'- {name["nombre"]} | id: {name["id"]}')
            
        id_task_edit = int(input('\nID de la tarea a editar: '))
        print(f'\nEditando...')
        
        if id_task_edit == name["id"]:
            name['nombre'] = input('\nNuevo nombre: ')
            name['descripcion'] = input('Nueva descripción: ')
            name['completado'] = input('¿Completado?: ')
            
            new_data = {"nombre": name['nombre'], "descripcion": name['descripcion'], 'completado': name['completado']}
            
            with open(file_search, 'w') as file:
                json.dump(task_data, file, indent=2)
                
            print('\nTarea editada con éxito.')
        else:
            print(f'\nLa tarea con el nombre < {id_task_edit} >, no existe.')
        
    def mark_task(self, user):
        print('\n:::: Marcar tareas ::::')
        
        try:
            file_search = f'task_{user}.json'
            with open(file_search, 'r') as file:
                task_data = json.load(file)
                
            if not task_data:
                print('\nNo hay tareas para marcar.')
            else:
                print('\nTareas: \n')
                for name in task_data:
                    print(f'- {name['nombre']} | id: {name['id']}')
                        
                id_task_mark = int(input('\nID de la tarea a marcar: '))
                
                for i, task in enumerate(task_data, 0):
                    if task['id'] == id_task_mark:
                        task['completado'] = 'Si'
                        print('\nTarea marcada con éxito.')
                        
                        with open(file_search, 'w') as file:
                            json.dump(task_data, file, indent=2)
    
        except Exception as e:
            print(f'\nHubo un error: > {e}')
            
    def uncheck_task(self, user):
        print('\n:::: Desmarcar tareas ::::')
        
        try:
            file_search = f'task_{user}.json'
            with open(file_search, 'r') as file:
                task_data = json.load(file)
                
            if not task_data:
                print('\nNo hay tareas para desmarcar.')
            else:
                print('\nTareas: \n')
                for name in task_data:
                    print(f'- {name['nombre']} | id: {name['id']}')
                        
                id_task_uncheck = int(input('\nID de la tarea a desmarcar: '))
                
                for task in task_data:
                    if task['id'] == id_task_uncheck:
                        task['completado'] = 'No'
                
                        with open(file_search, 'w') as file:
                            json.dump(task_data, file, indent=2)
                            
                        print('\nSe ha desmarcado la tarea.')
                         
        except Exception as e:
            print(f'\nHubo un error: > {e}')
   
    def show_task(self, user):
        print('\n:::: Mis Tareas ::::')
        
        try:
            file_search = f'task_{user}.json'
            with open(file_search, 'r') as file:
                task_data = json.load(file)
                
            if not task_data:
                print('\nNo tienes tareas.')
            else:
                for task in task_data:
                    show_data = f"\nNombre: {task['nombre']}\nDescripción: {task['descripcion']}\nCompletado: {task['completado']}"
                    
                    print(show_data)
                
        except Exception as e:
            print(e)
          
    def share_task(self, user):
        print('\n:::: Compartir tareas ::::')
        
        try:
            file_current = f'task_{user}.json'
            with open(file_current, 'r') as file:
                task_mydata = json.load(file)
                
            if not task_mydata:
                print('\nNo hay tareas aún.')
            else:
                print('\nTareas: \n')
                for name in task_mydata:
                    print(f'- {name["nombre"]} | id: {name["id"]} ')
                
                user_final = input('\nUsuario destino: ')
                id_task_share = int(input('ID de la tarea a compartir: '))
                
                for name in task_mydata:
                    if name["id"] == id_task_share:
                        task_final_data = []
                        
                        task_share = {'nombre': name['nombre'], 'descripcion': name['descripcion'], 'completado': name['completado'], 'id': name['id']}
                
                        file_final = f'task_{user_final}.json'
                        if os.path.getsize(file_final) > 0:
                            with open(file_final, 'r') as file:
                                task_final_data = json.load(file)
                                
                        task_final_data.append(task_share)
                        
                        with open(file_final, 'w') as file:
                            json.dump(task_final_data, file, indent=2)
                            
                        print('\nTarea compartida con éxito.')
            
        except Exception as e:
            print(e)
    
    # Create account and Log-in
    
    def create_account(self):
        print('\n:::: Crear cuenta :::: \n')
        
        name = str(input('Nombre: '))
        lastname = str(input('Apellido: '))
        username = str(input('Usuario: '))
        password = str(input('Contraseña: '))
        
        name_complete = f'{name.capitalize()} {lastname.capitalize()}'
        
        info_data = {'nombre_completo': name_complete, 'usuario': username.strip(), 'password': password.strip()}
        
        with open(f'{username}.json', 'w') as file:
            json.dump(info_data, file, indent=2)
            
        with open(f'task_{username}.json', 'w') as file:
            json.dump([], file, indent=2)
            
        print('\nCuenta creada con éxito.')
            
    def login(self):
        print('\n:::: Iniciar sesión ::::\n')
        
        user = str(input('Usuario: '))
        password = str(input('Contraseña: '))
        
        with open(f'{user}.json', 'r') as file_login:
            data_user = json.load(file_login)
        
        if user.strip() == data_user['usuario'] and password.strip() == data_user['password']:
            while True:
                print(f'\nHola, {data_user["nombre_completo"]}!\n¿Qué deseas hacer hoy?')
                
                menu = int(input('\n1. Crear tareas\n2. Eliminar tareas\n3. Editar tareas\n4. Marcar tareas\n5. Desmarcar tareas\n6. Ver tareas\n7. Compartir tareas\n8. Cerrar sesión\n\n> '))
                
                if menu == 1:
                    self.create_task(user)
                elif menu == 2: 
                    self.del_task(user)
                elif menu == 3:
                    self.edit_task(user)
                elif menu == 4:
                    self.mark_task(user)
                elif menu == 5:
                    self.uncheck_task(user)
                elif menu == 6:
                    self.show_task(user)
                elif menu == 7:
                    self.share_task(user)
                elif menu == 8:
                    print('\nSesión cerrada.')
                    break
                else:
                    print('\nNo existe ese rango')
        else:
            print('\nError: Datos incorrectos.')

    
task = MyTask()

try:
    while True:
        menu = int(input('\n1. Crear cuenta\n2. Iniciar sesión\n\n> '))
        
        if menu == 1:
            task.create_account()
        elif menu == 2:
            task.login()
        else:
            print('\nEse rango no existe.')
except Exception as e:
    print(f'\nHubo un error: {e}')
        
