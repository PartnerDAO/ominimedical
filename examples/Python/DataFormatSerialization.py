import json
from typing import List

class CDCSerializer:
    @staticmethod
    def to_json(observations: List[CDCObservation], 
                knowledge: List[CDCKnowledge],
                processes: List[CDCProcess]) -> str:
        """Serialize CDC data to JSON format"""
        data = {
            "observations": [obs.__dict__ for obs in observations],
            "knowledge": [know.__dict__ for know in knowledge],
            "process": [proc.__dict__ for proc in processes],
            "serialization_format": "CDC_JSON_1.0",
            "timestamp": datetime.now().isoformat()
        }
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    @staticmethod
    def from_json(json_data: str) -> tuple:
        """Deserialize CDC data from JSON format"""
        data = json.loads(json_data)
        
        observations = [CDCObservation(**obs) for obs in data.get('observations', [])]
        knowledge = [CDCKnowledge(**know) for know in data.get('knowledge', [])]
        processes = [CDCProcess(**proc) for proc in data.get('process', [])]
        
        return observations, knowledge, processes

# Example usage of serialization
def serialization_example():
    """Demonstrate CDC data serialization"""
    cdc = CDCProtocol()
    
    # Create some sample data
    observations = cdc.parse_to_observations("P001", "throbbing headache with nausea", "@Medicine@Neurology")
    knowledge = [cdc.load_knowledge("Migraine without aura", "ICHD-3")]
    processes = [
        CDCProcess("P001", "Headache", "r-Assessment@Medicine@Neurology", "Initial evaluation", 0.9, True)
    ]
    
    # Serialize to JSON
    json_output = CDCSerializer.to_json(observations, knowledge, processes)
    print("=== CDC JSON Serialization Example ===")
    print(json_output)
    
    # Deserialize back
    obs_back, know_back, proc_back = CDCSerializer.from_json(json_output)
    print(f"\nDeserialized: {len(obs_back)} observations, {len(know_back)} knowledge, {len(proc_back)} processes")
    
    return json_output