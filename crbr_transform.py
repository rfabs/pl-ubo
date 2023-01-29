import requests
import datetime
import json
import xmltodict
#import pprint
#import untangle
#import lxml.etree

CRBR_URL = "https://bramka-crbr.mf.gov.pl:5058/uslugiBiznesowe/uslugiESB/AP/ApiPrzegladoweCRBR/2022/02/01"

headers = {'content-type': 'application/soap+xml'}

def get_company(NIP: str):

    CMPY_BODY = f"""
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:ns="http://www.mf.gov.pl/uslugiBiznesowe/uslugiESB/AP/ApiPrzegladoweCRBR/2022/02/01"
    xmlns:ns1="http://www.mf.gov.pl/schematy/AP/ApiPrzegladoweCRBR/2022/02/01">
    <soap:Header/> <soap:Body>
            <ns:PobierzInformacjeOSpolkachIBeneficjentach>
                <PobierzInformacjeOSpolkachIBeneficjentachDane>
                    <ns1:SzczegolyWniosku>
                        <ns1:NIP>{NIP}</ns1:NIP>
                    </ns1:SzczegolyWniosku>
                </PobierzInformacjeOSpolkachIBeneficjentachDane>
            </ns:PobierzInformacjeOSpolkachIBeneficjentach>
        </soap:Body>
    </soap:Envelope>
    """

    response = requests.post(CRBR_URL, data=CMPY_BODY, headers=headers).text

    xml_data = xmltodict.parse(response,
                               encoding="utf-8",
                               process_namespaces=False,
                               namespace_separator=":")

    #json_data = json.dumps(xml_data, sort_keys=True, indent=2)
    #json_data = json.dumps(xml_data)

    return xml_data #json_data

#get_company(5261196513)

def get_person(PESEL: str):

    PERSON_BODY = f"""
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:ns="http://www.mf.gov.pl/uslugiBiznesowe/uslugiESB/AP/ApiPrzegladoweCRBR/2022/02/01"
    xmlns:ns1="http://www.mf.gov.pl/schematy/AP/ApiPrzegladoweCRBR/2022/02/01">
    <soap:Header/>
        <soap:Body>
            <ns:PobierzInformacjeOSpolkachIBeneficjentach>
                <PobierzInformacjeOSpolkachIBeneficjentachDane>
                    <ns1:SzczegolyWniosku>
                        <ns1:PESEL>{PESEL}</ns1:PESEL>
                    </ns1:SzczegolyWniosku>
                </PobierzInformacjeOSpolkachIBeneficjentachDane>
            </ns:PobierzInformacjeOSpolkachIBeneficjentach>
        </soap:Body>
    </soap:Envelope>
    """

    response = requests.post(CRBR_URL, data=PERSON_BODY, headers=headers).text

    data = xmltodict.parse(response,
                           encoding="utf-8",
                           process_namespaces=False,
                           namespace_separator=":")

    #json_data = json.dumps(xml_data, sort_keys=True, indent=2)
    #json_data = json.dumps(xml_data)

    return data #json_data



