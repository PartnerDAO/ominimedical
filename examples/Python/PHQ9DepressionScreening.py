@dataclass
class PHQ9Assessment:
    patient_id: str
    total_score: int
    severity: str
    recommendations: List[str]

class MentalHealthCDC:
    def __init__(self):
        self.phq9_items = {
            'anhedonia': {
                'question': 'Little interest or pleasure in doing things',
                'scores': {'Not at all': 0, 'Several days': 1, 'More than half the days': 2, 'Nearly every day': 3}
            },
            'depressed_mood': {
                'question': 'Feeling down, depressed, or hopeless', 
                'scores': {'Not at all': 0, 'Several days': 1, 'More than half the days': 2, 'Nearly every day': 3}
            }
            # ... other PHQ-9 items would be defined here
        }
    
    def parse_depression_symptoms(self, patient_id: str, utterance: str) -> List[CDCObservation]:
        """Parse patient utterances about mental health symptoms"""
        observations = []
        
        # Simulate LLM parsing of mental health symptoms
        symptoms_mapping = {
            'dont want to do things': ('Anhedonia', 'r-Symptom@Psychology@ClinicalPsychology'),
            'lost interest': ('Anhedonia', 'r-Symptom@Psychology@ClinicalPsychology'),
            'enjoyed anymore': ('Anhedonia', 'r-Symptom@Psychology@ClinicalPsychology'),
            'feel hopeless': ('Depressed Mood', 'r-Symptom@Psychology@ClinicalPsychology'),
            'feel down': ('Depressed Mood', 'r-Symptom@Psychology@ClinicalPsychology')
        }
        
        utterance_lower = utterance.lower()
        for keyword, (concept, relation) in symptoms_mapping.items():
            if keyword in utterance_lower:
                observations.append(CDCObservation(
                    patient_id=patient_id,
                    concept=concept,
                    relation=relation,
                    value=f"Reported: {utterance}",
                    timestamp=datetime.now().isoformat()
                ))
        
        return observations
    
    def load_depression_knowledge(self) -> CDCKnowledge:
        """Load DSM-5 criteria for depression"""
        return CDCKnowledge(
            concept="Major Depressive Episode",
            domain="@Psychology@ClinicalPsychology", 
            reference_standard="DSM-5",
            diagnostic_criteria=[
                "Depressed mood OR anhedonia (at least one required)",
                "Present most of the day, nearly every day", 
                "For at least 2 weeks",
                "Plus 4 additional symptoms from list"
            ]
        )
    
    def assess_phq9(self, observations: List[CDCObservation]) -> PHQ9Assessment:
        """Perform PHQ-9 assessment based on observations"""
        scores = []
        
        for obs in observations:
            if 'Anhedonia' in obs.concept:
                # In practice, this would come from structured assessment
                # For demo, we'll assign a score based on frequency language
                if 'every day' in obs.value.lower() or 'anymore' in obs.value.lower():
                    scores.append(3)  # Nearly every day
                else:
                    scores.append(2)  # More than half the days
        
        # For demo, add some additional scores
        total_score = sum(scores) + 12  # Simulating other symptoms
        
        # Determine severity
        if total_score >= 20:
            severity = "Severe depression"
            recommendations = ["Urgent psychiatric referral", "Therapy + medication evaluation"]
        elif total_score >= 15:
            severity = "Moderately severe depression" 
            recommendations = ["Therapy referral", "Consider medication", "Follow-up in 2 weeks"]
        elif total_score >= 10:
            severity = "Moderate depression"
            recommendations = ["Therapy consideration", "Lifestyle interventions", "Monitor symptoms"]
        else:
            severity = "Minimal depression"
            recommendations = ["Watchful waiting", "Self-care strategies"]
        
        return PHQ9Assessment(
            patient_id=observations[0].patient_id if observations else "Unknown",
            total_score=total_score,
            severity=severity,
            recommendations=recommendations
        )
    
    def create_depression_process(self, assessment: PHQ9Assessment) -> List[CDCProcess]:
        """Create CDC process records for depression assessment"""
        processes = []
        
        processes.append(CDCProcess(
            patient_id=assessment.patient_id,
            concept="PHQ-9",
            action="r-ScaleScore@Psychology@ClinicalPsychology", 
            value=f"Item 1 (Anhedonia): Score 3 (Nearly every day)"
        ))
        
        processes.append(CDCProcess(
            patient_id=assessment.patient_id,
            concept="PHQ-9", 
            action="r-TotalScore@Psychology@ClinicalPsychology",
            value=str(assessment.total_score)
        ))
        
        processes.append(CDCProcess(
            patient_id=assessment.patient_id,
            concept="Depression",
            action="r-Severity@Psychology@ClinicalPsychology",
            value=assessment.severity
        ))
        
        return processes

def depression_screening_example():
    mh_cdc = MentalHealthCDC()
    
    # Patient input
    patient_input = "I don't want to do things I used to enjoy anymore"
    
    # Step 1: Parse symptoms
    observations = mh_cdc.parse_depression_symptoms("S001", patient_input)
    
    # Step 2: Load knowledge
    knowledge = mh_cdc.load_depression_knowledge()
    
    # Step 3: Assess
    assessment = mh_cdc.assess_phq9(observations)
    
    # Step 4: Create process records
    processes = mh_cdc.create_depression_process(assessment)
    
    # Output results
    print("\n=== Depression Screening Example ===")
    print(f"PHQ-9 Total Score: {assessment.total_score}/27")
    print(f"Severity: {assessment.severity}")
    print("Recommendations:")
    for rec in assessment.recommendations:
        print(f"  - {rec}")
    print("Process Records:")
    for process in processes:
        print(f"  - {process.concept}: {process.action} -> {process.value}")
    
    return assessment, processes