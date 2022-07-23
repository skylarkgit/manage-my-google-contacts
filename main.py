from __future__ import print_function
from cred_util import sigin

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from text_util import format_name, get_first_name

messyFirstNameSet = {"Home", "C", "K", "S", "T", "Uk", "N", "R", "Kota"}

def main():
    creds = sigin()
    try:
        service = build('people', 'v1', credentials=creds)

        # Call the People API
        print('List 10 connection names')
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=200,
            personFields='names').execute()
        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            if names:
                fullName = names[0].get('displayName')
                firstName = get_first_name(names[0].get('givenName'))
                if firstName in messyFirstNameSet:
                    print('------------------------UPDATING---------------------------')
                    print(person)
                    final_name = format_name(fullName)
                    resource_name = person.get('resourceName')
                    service.people().updateContact(resourceName=resource_name, updatePersonFields="names", body={
                        "etag": person.get('etag'),
                        "names": {
                            "familyName": "",
                            "givenName": final_name,
                            "displayName": final_name
                        }
                        }).execute()
                    print(service.people().get(resourceName=resource_name, personFields='names').execute())
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()