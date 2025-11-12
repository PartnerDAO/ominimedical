@dataclass
class TreatmentProtocol:
    name: str
    domain: str
    version: str
    update_date: str
    criteria: List[str]
    source: str

class HospitalCDCSystem:
    def __init__(self, hospital_name: str):
        self.hospital_name = hospital_name
        self.local_knowledge = {}
        self.shared_protocols = {}
    
    def create_treatment_protocol(self, protocol: TreatmentProtocol) -> CDCKnowledge:
        """Create a CDC knowledge record for a treatment protocol"""
        cdc_knowledge = CDCKnowledge(
            concept=protocol.name,
            domain=protocol.domain,
            reference_standard=protocol.version,
            diagnostic_criteria=protocol.criteria
        )
        
        self.local_knowledge[protocol.name] = {
            'cdc_knowledge': cdc_knowledge,
            'metadata': protocol
        }
        
        return cdc_knowledge
    
    def export_protocol(self, protocol_name: str) -> Dict[str, Any]:
        """Export a protocol in CDC-compatible format"""
        if protocol_name not in self.local_knowledge:
            return None
            
        protocol_data = self.local_knowledge[protocol_name]
        return {
            'knowledge': protocol_data['cdc_knowledge'],
            'metadata': protocol_data['metadata'].__dict__,
            'export_format': 'CDC_1.0',
            'export_timestamp': datetime.now().isoformat()
        }
    
    def import_protocol(self, protocol_data: Dict[str, Any]) -> bool:
        """Import a protocol from another hospital"""
        try:
            # Verify CDC structure is valid
            if not self.verify_cdc_structure(protocol_data):
                return False
            
            knowledge_data = protocol_data['knowledge']
            metadata = protocol_data['metadata']
            
            # Create CDC knowledge record
            cdc_knowledge = CDCKnowledge(
                concept=knowledge_data['concept'],
                domain=knowledge_data['domain'],
                reference_standard=knowledge_data['reference_standard'],
                diagnostic_criteria=knowledge_data['diagnostic_criteria']
            )
            
            # Store in shared protocols
            protocol_name = knowledge_data['concept']
            self.shared_protocols[protocol_name] = {
                'cdc_knowledge': cdc_knowledge,
                'metadata': metadata,
                'imported_from': metadata.get('source', 'Unknown'),
                'import_date': datetime.now().isoformat()
            }
            
            print(f"✅ Successfully imported protocol: {protocol_name}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to import protocol: {e}")
            return False
    
    def verify_cdc_structure(self, protocol_data: Dict[str, Any]) -> bool:
        """Verify that CDC structure is valid"""
        required_keys = ['knowledge', 'metadata', 'export_format']
        if not all(key in protocol_data for key in required_keys):
            return False
        
        knowledge = protocol_data['knowledge']
        required_knowledge_keys = ['concept', 'domain', 'reference_standard', 'diagnostic_criteria']
        if not all(key in knowledge for key in required_knowledge_keys):
            return False
        
        return True
    
    def apply_treatment_protocol(self, patient_id: str, protocol_name: str) -> List[CDCProcess]:
        """Apply a treatment protocol to a patient"""
        if protocol_name not in self.shared_protocols:
            print(f"Protocol {protocol_name} not found")
            return []
        
        protocol = self.shared_protocols[protocol_name]
        processes = []
        
        processes.append(CDCProcess(
            patient_id=patient_id,
            concept=protocol_name,
            action="r-TreatmentInitiation@Medicine@InfectiousDiseases",
            value=f"Applied protocol {protocol_name}",
            confidence=0.95,
            verified=True
        ))
        
        # Simulate protocol application steps
        for i, criterion in enumerate(protocol['cdc_knowledge'].diagnostic_criteria):
            processes.append(CDCProcess(
                patient_id=patient_id,
                concept=protocol_name,
                action=f"r-CriterionCheck@Medicine@InfectiousDiseases",
                value=f"Criterion {i+1}: {criterion}",
                verified=True
            ))
        
        return processes

def cross_hospital_example():
    # Hospital A (Boston) creates a new protocol
    boston_hospital = HospitalCDCSystem("Boston General Hospital")
    
    covid_protocol = TreatmentProtocol(
        name="COVID-19 Treatment Protocol v2.3",
        domain="@Medicine@InfectiousDiseases", 
        version="2.3",
        update_date="2024-10-15",
        criteria=[
            "New antiviral shows 40% better outcomes",
            "Recommended for high-risk patients >65 years",
            "5-day course with monitoring"
        ],
        source="Harvard Medical School Clinical Trial #12345"
    )
    
    # Hospital A creates and exports the protocol
    boston_hospital.create_treatment_protocol(covid_protocol)
    exported_data = boston_hospital.export_protocol("COVID-19 Treatment Protocol v2.3")
    
    # Hospital B (Shanghai) imports the protocol
    shanghai_hospital = HospitalCDCSystem("Shanghai Medical Center")
    import_success = shanghai_hospital.import_protocol(exported_data)
    
    if import_success:
        # Hospital B applies the protocol to a patient
        processes = shanghai_hospital.apply_treatment_protocol("P002", "COVID-19 Treatment Protocol v2.3")
        
        print("\n=== Cross-Hospital Knowledge Sharing Example ===")
        print(f"Hospital A ({boston_hospital.hospital_name}): Created COVID-19 protocol")
        print(f"Hospital B ({shanghai_hospital.hospital_name}): Imported and applied protocol")
        print("Application Process:")
        for process in processes:
            print(f"  - {process.action}: {process.value}")
    
    return import_success