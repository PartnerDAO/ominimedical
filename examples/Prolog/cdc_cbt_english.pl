% =====================================================================
% CDC+CBT Isomorphic Transformation System: Complete Demonstration Based on 10-Round Dialogue
% Core: CDC Structure ↔ CBT Theory Isomorphic Mapping
% =====================================================================

% ===== 1. CDC Data from 10 Rounds of Dialogue in the Document =====

% Round 1: Zhang San's First Input
cdc_raw(1, 'work pressure', 'CBT situation', 'triggers', 'negative self-evaluation').
cdc_raw(1, 'can\'t do anything right', 'CBT cognition', 'manifests_as', 'all-or-nothing thinking').

% Round 2: Specific Event Description
cdc_raw(2, 'project bug', 'CBT event', 'leads_to', 'long debugging').
cdc_raw(2, 'requirement misunderstanding', 'CBT event', 'leads_to', 'rework').
cdc_raw(2, 'two events', 'CBT cognition', 'generalized_to', 'useless programmer').

% Round 3: Positive Evidence Appears
cdc_raw(3, 'independent module completion', 'CBT fact', 'positive_evidence', 'capability proof').
cdc_raw(3, 'colleague recognition', 'CBT fact', 'external_validation', 'code quality').
cdc_raw(3, 'performance optimization success', 'CBT fact', 'positive_evidence', 'technical ability').
cdc_raw(3, 'good luck attribution', 'CBT cognition', 'manifests_as', 'success discounting').

% Round 4: Cognitive Change Begins
cdc_raw(4, 'performance optimization', 'CBT reappraisal', 'requires', 'analytical ability').
cdc_raw(4, 'fear of making mistakes', 'CBT emotion', 'manifests_as', 'anxiety anticipation').
cdc_raw(4, 'worried about screwing up next time', 'CBT cognition', 'type_of', 'catastrophic thinking').

% Round 5: Double Standard Discovery
cdc_raw(5, 'others make mistakes', 'CBT cognition', 'perceived_as', 'normal phenomenon').
cdc_raw(5, 'I make mistakes', 'CBT cognition', 'perceived_as', 'particularly noticeable').
cdc_raw(5, 'considered unprofessional', 'CBT cognition', 'type_of', 'mind reading').
cdc_raw(5, 'double standard', 'CBT cognition', 'manifests_as', 'self-demanding').

% Round 6: Reality Check
cdc_raw(6, 'no direct negative evaluation', 'CBT fact', 'contradicts', 'mind reading prediction').
cdc_raw(6, 'lead positive evaluation', 'CBT fact', 'supports', 'professional ability').
cdc_raw(6, 'thorough code review', 'CBT fact', 'evidence_of', 'work quality').
cdc_raw(6, 'overthinking', 'CBT metacognition', 'awareness_of', 'cognitive bias').

% Round 7: Perfectionism Identification
cdc_raw(7, 'overthinking', 'CBT metacognition', 'self_awareness', 'thinking pattern').
cdc_raw(7, 'hard to accept mistakes', 'CBT cognition', 'manifests_as', 'perfectionism').
cdc_raw(7, 'should do better', 'CBT cognition', 'type_of', 'absolutistic demands').
cdc_raw(7, 'anxiety when not achieved', 'CBT emotion', 'result_of', 'perfectionism').

% Round 8: Standard Adjustment
cdc_raw(8, 'complete tasks on time', 'CBT standard', 'realistic_expectation', 'basic requirement').
cdc_raw(8, 'code quality meets standards', 'CBT standard', 'realistic_expectation', 'team standard').
cdc_raw(8, 'timely problem fixing', 'CBT standard', 'realistic_expectation', 'response ability').
cdc_raw(8, 'zero errors not needed', 'CBT cognition', 'rational_belief', 'realistic expectation').

% Round 9: Self-Reappraisal
cdc_raw(9, 'complete tasks on time', 'CBT self-evaluation', 'achieves', 'reasonable standard').
cdc_raw(9, 'code review passed', 'CBT self-evaluation', 'achieves', 'quality standard').
cdc_raw(9, 'quick bug fixing', 'CBT self-evaluation', 'achieves', 'response standard').
cdc_raw(9, 'performance is okay', 'CBT cognition', 'realistic_assessment', 'self-evaluation').

% Round 10: Treatment Effect
cdc_raw(10, 'ordinary programmer', 'CBT cognition', 'balanced_view', 'real self').
cdc_raw(10, 'has strengths and weaknesses', 'CBT cognition', 'balanced_assessment', 'objective evaluation').
cdc_raw(10, 'makes mistakes and grows', 'CBT cognition', 'growth_mindset', 'developmental perspective').
cdc_raw(10, 'no longer feeling worthless', 'CBT cognition', 'cognitive_change', 'core transformation').
cdc_raw(10, 'relaxed mood', 'CBT emotion', 'improvement', 'treatment effect').

% ===== 2. CDC to CBT Isomorphic Mapping Rules =====

% CBT Cognitive Pattern Recognition Rules
cbt_pattern_rule('all-or-nothing thinking') :-
    cdc_raw(_, _, 'CBT cognition', 'manifests_as', 'all-or-nothing thinking').

cbt_pattern_rule('overgeneralization') :-
    cdc_raw(_, _, 'CBT cognition', 'generalized_to', _).

cbt_pattern_rule('discounting the positive') :-
    cdc_raw(_, _, 'CBT cognition', 'manifests_as', 'success discounting').

cbt_pattern_rule('catastrophic thinking') :-
    cdc_raw(_, _, 'CBT cognition', 'type_of', 'catastrophic thinking').

cbt_pattern_rule('mind reading') :-
    cdc_raw(_, _, 'CBT cognition', 'type_of', 'mind reading').

cbt_pattern_rule('perfectionism') :-
    cdc_raw(_, _, 'CBT cognition', 'manifests_as', 'perfectionism').

% Therapy Progress Mapping
therapy_progress_rule('cognitive restructuring') :-
    cdc_raw(_, _, 'CBT reappraisal', 'requires', _).

therapy_progress_rule('reality testing') :-
    cdc_raw(_, _, 'CBT fact', 'contradicts', _).

therapy_progress_rule('metacognitive awareness') :-
    cdc_raw(_, _, 'CBT metacognition', 'awareness_of', _).

therapy_progress_rule('standard adjustment') :-
    cdc_raw(_, _, 'CBT standard', 'realistic_expectation', _).

% ===== 3. Core Analysis Engine =====

% Main Analysis Function: CDC → CBT Diagnosis
analyze_patient_cdc(Patient, Analysis) :-
    identify_cognitive_patterns(Patient, Patterns),
    identify_therapy_progress(Patient, Progress),
    calculate_improvement_metrics(Patient, Metrics),
    generate_treatment_recommendations(Patient, Recommendations),
    Analysis = analysis(Patterns, Progress, Metrics, Recommendations).

% Identify Cognitive Patterns
identify_cognitive_patterns(_Patient, Patterns) :-
    findall(Pattern-Turn-Severity, (
        cdc_raw(Turn, Concept1, Domain, Relation, Concept2),
        map_cdc_to_pattern(Concept1, Domain, Relation, Concept2, Pattern, Severity)
    ), PatternList),
    group_patterns_by_type(PatternList, Patterns).

% CDC to Cognitive Pattern Mapping
map_cdc_to_pattern(_, 'CBT cognition', 'manifests_as', 'all-or-nothing thinking', 'all-or-nothing thinking', 0.8).
map_cdc_to_pattern(_, 'CBT cognition', 'generalized_to', _, 'overgeneralization', 0.7).
map_cdc_to_pattern(_, 'CBT cognition', 'manifests_as', 'success discounting', 'discounting the positive', 0.6).
map_cdc_to_pattern(_, 'CBT cognition', 'type_of', 'catastrophic thinking', 'catastrophic thinking', 0.7).
map_cdc_to_pattern(_, 'CBT cognition', 'type_of', 'mind reading', 'mind reading', 0.6).
map_cdc_to_pattern(_, 'CBT cognition', 'manifests_as', 'perfectionism', 'perfectionism', 0.8).

% Identify Therapy Progress
identify_therapy_progress(_Patient, Progress) :-
    findall(Stage-Turn, (
        cdc_raw(Turn, _, Domain, Relation, _),
        map_cdc_to_progress_stage(Domain, Relation, Stage)
    ), ProgressList),
    sort(ProgressList, Progress).

% CDC to Therapy Stage Mapping
map_cdc_to_progress_stage('CBT reappraisal', 'requires', 'cognitive restructuring').
map_cdc_to_progress_stage('CBT fact', 'contradicts', 'reality testing').
map_cdc_to_progress_stage('CBT metacognition', 'awareness_of', 'metacognitive awareness').
map_cdc_to_progress_stage('CBT standard', 'realistic_expectation', 'standard adjustment').
map_cdc_to_progress_stage('CBT cognition', 'cognitive_change', 'core change').

% Calculate Improvement Metrics
calculate_improvement_metrics(_Patient, Metrics) :-
    count_negative_patterns(NegativeCount),
    count_positive_changes(PositiveCount),
    count_evidence_balance(EvidenceRatio),
    EmotionalImprovement is PositiveCount / (NegativeCount + 1),
    Metrics = metrics(NegativeCount, PositiveCount, EvidenceRatio, EmotionalImprovement).

count_negative_patterns(Count) :-
    findall(1, (
        cdc_raw(_, _, 'CBT cognition', Relation, _),
        member(Relation, ['manifests_as', 'type_of', 'generalized_to'])
    ), List),
    length(List, Count).

count_positive_changes(Count) :-
    findall(1, (
        cdc_raw(_, _, Domain, _, _),
        member(Domain, ['CBT reappraisal', 'CBT metacognition', 'CBT standard'])
    ), List),
    length(List, Count).

count_evidence_balance(Ratio) :-
    findall(1, cdc_raw(_, _, 'CBT fact', 'positive_evidence', _), PosList),
    findall(1, cdc_raw(_, _, 'CBT fact', 'negative_evidence', _), NegList),
    length(PosList, PosCount),
    length(NegList, NegCount),
    (NegCount > 0 -> Ratio is PosCount / NegCount; Ratio = 3.0).

% Generate Treatment Recommendations
generate_treatment_recommendations(Patient, Recommendations) :-
    identify_cognitive_patterns(Patient, Patterns),
    findall(Recommendation, (
        member(Pattern-_-Severity, Patterns),
        Severity > 0.5,
        pattern_to_intervention(Pattern, Recommendation)
    ), Recommendations).

% Cognitive Pattern to Intervention Method Mapping
pattern_to_intervention('all-or-nothing thinking', 'gray thinking exercises').
pattern_to_intervention('overgeneralization', 'evidence collection and balancing').
pattern_to_intervention('discounting the positive', 'positive attribution training').
pattern_to_intervention('catastrophic thinking', 'probability assessment techniques').
pattern_to_intervention('mind reading', 'reality testing exercises').
pattern_to_intervention('perfectionism', 'reasonable standard setting').

% ===== 4. Demonstration and Output Interface =====

% Full Analysis Demonstration
demo_full_analysis :-
    write('=== CDC+CBT Isomorphic Analysis Demonstration ==='), nl,
    analyze_patient_cdc('Zhang San', Analysis),
    display_analysis_results(Analysis).

% Display Analysis Results
display_analysis_results(analysis(Patterns, Progress, Metrics, Recommendations)) :-
    write('== Identified Cognitive Patterns =='), nl,
    display_patterns(Patterns), nl,
    write('== Therapy Progress Trajectory =='), nl,
    display_progress(Progress), nl,
    write('== Improvement Metrics =='), nl,
    display_metrics(Metrics), nl,
    write('== Treatment Recommendations =='), nl,
    display_recommendations(Recommendations).

display_patterns([]).
display_patterns([Pattern-Turn-Severity|Rest]) :-
    format('  Round ~w: ~w (Severity: ~2f)~n', [Turn, Pattern, Severity]),
    display_patterns(Rest).

display_progress([]).
display_progress([Stage-Turn|Rest]) :-
    format('  Round ~w: ~w~n', [Turn, Stage]),
    display_progress(Rest).

display_metrics(metrics(Neg, Pos, Ratio, Improvement)) :-
    format('  Negative patterns count: ~w~n', [Neg]),
    format('  Positive changes count: ~w~n', [Pos]),
    format('  Evidence balance ratio: ~2f~n', [Ratio]),
    format('  Emotional improvement degree: ~2f~n', [Improvement]).

display_recommendations([]).
display_recommendations([Rec|Rest]) :-
    format('  - ~w~n', [Rec]),
    display_recommendations(Rest).

% Analyze by Round
analyze_by_turn(Turn) :-
    format('=== CDC Structure for Round ~w ===~n', [Turn]),
    findall(cdc(C1, Domain, Relation, C2),
        cdc_raw(Turn, C1, Domain, Relation, C2),
        CDCs),
    display_cdc_structures(CDCs),
    format('=== Corresponding CBT Analysis ===~n'),
    analyze_turn_cbt_patterns(Turn).

display_cdc_structures([]).
display_cdc_structures([cdc(C1, Domain, Relation, C2)|Rest]) :-
    format('  ~w --[~w:~w]--> ~w~n', [C1, Domain, Relation, C2]),
    display_cdc_structures(Rest).

analyze_turn_cbt_patterns(Turn) :-
    findall(Pattern, (
        cdc_raw(Turn, C1, Domain, Relation, C2),
        map_cdc_to_pattern(C1, Domain, Relation, C2, Pattern, _)
    ), Patterns),
    (Patterns = [] ->
        write('  No obvious cognitive patterns');
        format('  Identified patterns: ~w~n', [Patterns])
    ).

% Utility Function: Pattern Grouping
group_patterns_by_type(PatternList, GroupedPatterns) :-
    findall(Pattern-Turns-AvgSeverity, (
        member(Pattern-Turn-Severity, PatternList),
        findall(T-S, member(Pattern-T-S, PatternList), TurnSeverityPairs),
        findall(T, member(T-_, TurnSeverityPairs), Turns),
        findall(S, member(_-S, TurnSeverityPairs), Severities),
        sum_list(Severities, SumSev),
        length(Severities, Count),
        AvgSeverity is SumSev / Count
    ), GroupedPatterns0),
    sort(GroupedPatterns0, GroupedPatterns).

% ===== 5. Quick Test Interface =====

% Quick Test All Functions
quick_test :-
    write('=== CDC+CBT System Quick Test ==='), nl,
    demo_full_analysis, nl,
    write('=== Detailed Analysis by Round ==='), nl,
    analyze_by_turn(1), nl,
    analyze_by_turn(5), nl,
    analyze_by_turn(10), nl.

% Verify Isomorphic Mapping
verify_isomorphism :-
    write('=== Verify CDC↔CBT Isomorphism ==='), nl,
    findall(Pattern, cbt_pattern_rule(Pattern), CBTPatterns),
    findall(Progress, therapy_progress_rule(Progress), ProgressStages),
    format('Found CBT patterns: ~w~n', [CBTPatterns]),
    format('Treatment stages: ~w~n', [ProgressStages]),
    length(CBTPatterns, PatternCount),
    length(ProgressStages, StageCount),
    format('Isomorphic mapping completeness: ~w patterns, ~w stages~n', [PatternCount, StageCount]).

% =====================================================================
% Usage:
% ?- quick_test.              % Run complete demonstration
% ?- demo_full_analysis.      % Display analysis results
% ?- analyze_by_turn(3).      % Analyze specific round
% ?- verify_isomorphism.      % Verify isomorphic mapping
% =====================================================================