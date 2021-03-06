from http.server import BaseHTTPRequestHandler, HTTPServer
from views.customers_requests import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer, get_customers_by_email
from views.locations_requests import get_all_locations, get_single_location, create_location, delete_location, update_location
from views.animal_requests import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_animals_by_location, get_animals_by_status
from views.employees_requests import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee, get_employees_by_location
import json


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """parses the URL"""
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)
   

#  def parse_url(self, path):
#         """parses the URL"""
#         path_params = path.split("/")
#         resource = path_params[1]
#         id = None

#         try:
#             id = int(path_params[2])
#         except IndexError:
#             pass  
#         except ValueError:
#             pass  

#         return (resource, id)
   
    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    # def do_GET(self):
    #     """Handles GET requests to the server
    #     """
    #     self._set_headers(200)
    #     response = {}
        
    #     (resource, id) = self.parse_url(self.path)

    #     if resource == "animals":
    #         if id is not None:
    #             response = f"{get_single_animal(id)}"
    #         else:
    #             response = f"{get_all_animals()}"
    
    #     if resource == "locations":
    #         if id is not None:
    #             response = f"{get_single_location(id)}"

    #         else:
    #             response = f"{get_all_locations()}"
        
    #     if resource == "employees":
    #         if id is not None:
    #             response = f"{get_single_employee(id)}"
    #         else:
    #             response = f"{get_all_employees()}"
                
    #     if resource == "customers":
    #         if id is not None:
    #             response = f"{get_single_customer(id)}"
    #         else:
    #             response = f"{get_all_customers()}"
                
    #     # print(f"this is the path {self.path}")
    #     # print(f"resource = {resource}, id = {id}")

        

    #     self.wfile.write(response.encode())
    #     print(self.path)
    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was for
        # `/animals` or `/animals/2`
        if len(parsed) == 2:
            ( resource, id ) = parsed# pylint: disable=unbalanced-tuple-unpacking

            if resource == "animals":
                if id is not None:
                    response = f"{get_single_animal(id)}"
                else:
                    response = f"{get_all_animals()}"
            elif resource == "customers":
                if id is not None:
                    response = f"{get_single_customer(id)}"
                else:
                    response = f"{get_all_customers()}"
            elif resource == "locations":
                if id is not None:
                    response = f"{get_single_location(id)}"
                else:
                    response = f"{get_all_locations()}"
            elif resource == "employees":
                if id is not None:
                    response = f"{get_single_employee(id)}"
                else:
                    response = f"{get_all_employees()}"
        # Response from parse_url() is a tuple with 3
        # items in it, which means the request was for
        # `/resource?parameter=value`
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            # Is the resource `customers` and was there a
            # query parameter that specified the customer
            # email as a filtering value?
            if key == "email" and resource == "customers":
                response = get_customers_by_email(value)
            if key == "location_id" and resource == "employees":
                response = get_employees_by_location(value)
            if key == "location_id" and resource == "animals":
                response = get_animals_by_location(value)
            if key == "status" and resource == "animals":
                response = get_animals_by_status(value)
                
        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)# pylint: disable=unbalanced-tuple-unpacking

        response = None
        
        if resource == "customers":
            response = create_customer(post_body)
            
        if resource == "animals":
            response = create_animal(post_body)
        
        if resource == "employees":
            response = create_employee(post_body)
            
        if resource == "locations":
            response = create_location(post_body)
        # new_location = None
        # if resource == "locations":
        #     new_location = create_location(post_body)

        #     self.wfile.write(f"{new_location}".encode())
        
            
        self.wfile.write(f"{response}".encode())
        
    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)# pylint: disable=unbalanced-tuple-unpacking

        if resource == "animals":
            delete_animal(id)
        if resource == "customers":
            delete_customer(id)
        if resource == "locations":
            delete_location(id)
        if resource == "employees":
            delete_employee(id)   
            
        self.wfile.write("".encode())
        
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)# pylint: disable=unbalanced-tuple-unpacking

        if resource == "animals":
            update_animal(id, post_body)

        if resource == "customers":
            update_customer(id, post_body)
            
        if resource == "employees":
            update_employee(id, post_body)
            
        if resource == "locations":
            update_location(id, post_body)
            
        self.wfile.write("".encode())
        
#def test_funct():
#   print("hello world")

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
#    test_funct()
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
