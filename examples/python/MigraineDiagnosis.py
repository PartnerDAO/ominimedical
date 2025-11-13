from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class CDCObservation:
    patient_id: str
    concept: str
    relation: str
    value: str
    timestamp: str

@dataclass
class CDCKnowledge:
    concept: str
    domain: str
    reference_standard: str
    diagnostic_criteria: List[str]

@dataclass
class CDCProcess:
    patient_id: str
    concept: str
    action: str
    value: str
    confidence: float = None
    verified: bool = False

@dataclass
class CDCDiagnosis:
    conclusion: str
    reasoning_chain: List[str]
    confidence: float
    verification_status: str

class CDCProtocol:
    def parse_to_observations(self, patient_id: str, utterance: str, domain: str) -> List[CDCObservation]:
        """Parse natural language patient input into CDC observations"""
        observations = []
        
        # Simulating LLM parsing - in practice this would use an actual LLM
        if "throbbing headache" in utterance.lower() and "left" in utterance.lower():
            observations.append(CDCObservation(
                patient_id=patient_id,
                concept="Headache",
                relation="r-FindingSite@Medicine@Neurology",
                value="Left temporal region",
                timestamp=datetime.now().isoformat()
            ))
            observations.append(CDCObservation(
                patient_id=patient_id,
                concept="Headache", 
                relation="r-AssociatedMorphology@Medicine@Neurology",
                value="Throbbing pain",
                timestamp=datetime.now().isoformat()
            ))
        
        if "nausea" in utterance.lower():
            observations.append(CDCObservation(
                patient_id=patient_id,
                concept="Headache",
                relation="r-AssociatedFinding@Medicine@Neurology", 
                value="Nausea",
                timestamp=datetime.now().isoformat()
            ))
            
        if "hours" in utterance.lower():
            # Extract duration - simplified
            observations.append(CDCObservation(
                patient_id=patient_id,
                concept="Headache",
                relation="r-Duration@Medicine@Neurology",
                value="6 hours",
                timestamp=datetime.now().isoformat()
            ))
            
        return observations

    def load_knowledge(self, concept: str, standard: str) -> CDCKnowledge:
        """Load medical knowledge standards"""
        if concept == "Migraine without aura" and standard == "ICHD-3":
            return CDCKnowledge(
                concept="Migraine without aura",
                domain="@Medicine@Neurology",
                reference_standard="ICHD-3 1.1",
                diagnostic_criteria=[
                    "Unilateral location",
                    "Pulsating quality", 
                    "Moderate to severe intensity",
                    "Nausea and/or vomiting OR photophobia and phonophobia",
                    "Duration 4-72 hours"
                ]
            )
        return None

    def reason(self, observations: List[CDCObservation], knowledge: CDCKnowledge) -> CDCDiagnosis:
        """Perform CDC reasoning and verification"""
        reasoning_chain = []
        criteria_met = 0
        total_criteria = len(knowledge.diagnostic_criteria)
        
        # Check each observation against diagnostic criteria
        for obs in observations:
            if "Left temporal region" in obs.value:
                reasoning_chain.append("Meets ICHD-3 criteria C.1 (unilateral location)")
                criteria_met += 1
            elif "Throbbing pain" in obs.value:
                reasoning_chain.append("Meets ICHD-3 criteria C.2 (pulsating quality)") 
                criteria_met += 1
            elif "Nausea" in obs.value:
                reasoning_chain.append("Meets ICHD-3 criteria D.1 (nausea)")
                criteria_met += 1
            elif "6 hours" in obs.value:
                reasoning_chain.append("Meets ICHD-3 duration criteria (4-72 hours)")
                criteria_met += 1
        
        confidence = criteria_met / total_criteria if total_criteria > 0 else 0
        verified = criteria_met >= 3  # Simplified verification logic
        
        return CDCDiagnosis(
            conclusion="Migraine without aura",
            reasoning_chain=reasoning_chain,
            confidence=round(confidence, 2),
            verification_status="VERIFIED" if verified else "REQUIRES_REVIEW"
        )

# Usage Example
def migraine_diagnosis_example():
    cdc = CDCProtocol()
    
    # Patient input
    patient_input = "I have a throbbing headache on my left side with nausea for 6 hours"
    
    # Step 1: Parse to CDC structure
    observations = cdc.parse_to_observations(
        patient_id="P001",
        utterance=patient_input,
        domain="@Medicine@Neurology"
    )
    
    # Step 2: Load medical knowledge
    knowledge = cdc.load_knowledge("Migraine without aura", "ICHD-3")
    
    # Step 3: Reason and diagnose
    diagnosis = cdc.reason(observations, knowledge)
    
    # Output results
    print("=== Migraine Diagnosis Example ===")
    print(f"Conclusion: {diagnosis.conclusion}")
    print(f"Confidence: {diagnosis.confidence}")
    print(f"Verification Status: {diagnosis.verification_status}")
    print("Reasoning Chain:")
    for step in diagnosis.reasoning_chain:
        print(f"  - {step}")
    
    return diagnosis