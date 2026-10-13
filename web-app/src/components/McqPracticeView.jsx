import React, { useState } from 'react';
import MathText from './MathText';
import { 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  Lightbulb, 
  RotateCcw, 
  Filter, 
  Award,
  BookOpen
} from 'lucide-react';

export default function McqPracticeView({ mcqBank, allNotes, onSelectTopic }) {
  const [selectedSubject, setSelectedSubject] = useState('ALL');
  const [filterStatus, setFilterStatus] = useState('ALL'); // 'ALL', 'CORRECT', 'WRONG', 'UNATTEMPTED'
  const [userAnswers, setUserAnswers] = useState({});
  const [showExplanations, setShowExplanations] = useState({});

  // Parse raw text of MCQ into structured fields
  const parseQuestion = (rawText) => {
    try {
      const parts = rawText.split(/\(a\)|\(b\)|\(c\)|\(d\)|Correct Answer:/);
      const question = parts[0].trim();
      const optA = parts[1] ? parts[1].trim() : '';
      const optB = parts[2] ? parts[2].trim() : '';
      const optC = parts[3] ? parts[3].trim() : '';
      const rest = parts[4] ? parts[4].trim() : '';
      
      let optD = rest;
      let answerExplanation = '';
      if (rawText.includes('Correct Answer:')) {
        const idx = rawText.indexOf('Correct Answer:');
        answerExplanation = rawText.substring(idx).trim();
      }

      let correctKey = '';
      if (answerExplanation.includes('(a)')) correctKey = 'a';
      else if (answerExplanation.includes('(b)')) correctKey = 'b';
      else if (answerExplanation.includes('(c)')) correctKey = 'c';
      else if (answerExplanation.includes('(d)')) correctKey = 'd';

      let explanation = answerExplanation;
      const match = answerExplanation.match(/\[Explanation:\s*(.*?)\]/i);
      if (match) explanation = match[1];

      return {
        question,
        options: { a: optA, b: optB, c: optC, d: optD.split(/Correct Answer:/)[0].trim() },
        correctKey,
        explanation
      };
    } catch (e) {
      return null;
    }
  };

  const parsedBank = mcqBank.map((item, index) => ({
    id: `mcq-bank-${index}`,
    ...item,
    parsed: parseQuestion(item.raw_text)
  })).filter(item => item.parsed !== null);

  const subjects = ['ALL', ...new Set(parsedBank.map(q => q.subject_title))];

  // Filtering
  const filteredList = parsedBank.filter(q => {
    const matchesSubject = selectedSubject === 'ALL' || q.subject_title === selectedSubject;
    const answeredKey = userAnswers[q.id];
    let matchesStatus = true;
    if (filterStatus === 'CORRECT') {
      matchesStatus = answeredKey && answeredKey === q.parsed.correctKey;
    } else if (filterStatus === 'WRONG') {
      matchesStatus = answeredKey && answeredKey !== q.parsed.correctKey;
    } else if (filterStatus === 'UNATTEMPTED') {
      matchesStatus = !answeredKey;
    }
    return matchesSubject && matchesStatus;
  });

  // Calculate score statistics
  const totalAttempted = Object.keys(userAnswers).length;
  const totalCorrect = Object.entries(userAnswers).filter(([id, ans]) => {
    const q = parsedBank.find(item => item.id === id);
    return q && q.parsed.correctKey === ans;
  }).length;
  const accuracy = totalAttempted > 0 ? Math.round((totalCorrect / totalAttempted) * 100) : 0;

  const handleSelectOption = (qId, key) => {
    setUserAnswers(prev => ({ ...prev, [qId]: key }));
    setShowExplanations(prev => ({ ...prev, [qId]: true }));
  };

  const toggleExplanation = (qId) => {
    setShowExplanations(prev => ({ ...prev, [qId]: !prev[qId] }));
  };

  const handleResetQuiz = () => {
    if (window.confirm('Reset all your practice MCQ answers and score?')) {
      setUserAnswers({});
      setShowExplanations({});
    }
  };

  return (
    <div className="flex-1 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-fade-in">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 mb-8 border-b border-[#2d2f3c]">
        <div>
          <span className="badge badge-amber mb-2">Screening Exam Preparation</span>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            APPSC Screening Objective Question Bank
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            290 authentic syllabus-mapped MCQs with verified answer keys and detailed explanations.
          </p>
        </div>

        {/* Scorecard */}
        <div className="flex items-center gap-3 bg-[#191b22] border border-[#2b2d39] p-3 rounded-xl shrink-0">
          <div className="text-center px-2">
            <div className="text-xs text-slate-400 font-medium">Attempted</div>
            <div className="text-lg font-bold text-white font-mono">{totalAttempted}/{parsedBank.length}</div>
          </div>
          <div className="h-8 w-px bg-[#2b2d39]"></div>
          <div className="text-center px-2">
            <div className="text-xs text-slate-400 font-medium">Score</div>
            <div className="text-lg font-bold text-emerald-400 font-mono">{totalCorrect}</div>
          </div>
          <div className="h-8 w-px bg-[#2b2d39]"></div>
          <div className="text-center px-2">
            <div className="text-xs text-slate-400 font-medium">Accuracy</div>
            <div className="text-lg font-bold text-sky-400 font-mono">{accuracy}%</div>
          </div>
          <button
            onClick={handleResetQuiz}
            className="p-2 ml-1 text-slate-400 hover:text-rose-400 hover:bg-[#252733] rounded-lg transition-colors"
            title="Reset Quiz"
          >
            <RotateCcw size={16} />
          </button>
        </div>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap items-center justify-between gap-3 mb-6 bg-[#181920] p-3 rounded-xl border border-[#2b2d39]">
        {/* Subject Filter */}
        <div className="flex items-center gap-2 overflow-x-auto pb-1 max-w-full">
          <Filter size={14} className="text-slate-400 shrink-0" />
          <span className="text-xs font-semibold text-slate-400 shrink-0">Subject:</span>
          <select
            value={selectedSubject}
            onChange={(e) => setSelectedSubject(e.target.value)}
            className="bg-[#20222d] border border-[#303343] text-xs text-white rounded-lg px-2.5 py-1.5 focus:outline-none focus:border-sky-400 max-w-xs"
          >
            {subjects.map((s, idx) => (
              <option key={idx} value={s}>
                {s === 'ALL' ? 'All 8 Subject Domains (290 Qs)' : s}
              </option>
            ))}
          </select>
        </div>

        {/* Status Filter */}
        <div className="flex items-center gap-1.5 text-xs">
          {['ALL', 'UNATTEMPTED', 'CORRECT', 'WRONG'].map(st => (
            <button
              key={st}
              onClick={() => setFilterStatus(st)}
              className={`px-2.5 py-1 rounded-md font-medium transition-colors ${
                filterStatus === st 
                  ? 'bg-sky-500 text-white shadow-sm' 
                  : 'bg-[#22242e] text-slate-400 hover:text-white'
              }`}
            >
              {st}
            </button>
          ))}
        </div>
      </div>

      {/* Questions List */}
      <div className="space-y-6">
        {filteredList.map((item, qIdx) => {
          const qId = item.id;
          const { question, options, correctKey, explanation } = item.parsed;
          const selected = userAnswers[qId];
          const isRevealed = showExplanations[qId];
          const isCorrect = selected === correctKey;

          return (
            <div 
              key={qId}
              className="bg-[#1b1c24] border border-[#2d2f3c] rounded-xl p-5 md:p-6 shadow-md hover:border-[#3d4052] transition-colors"
            >
              {/* Question Meta */}
              <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span className="text-[11px] font-mono text-sky-400 uppercase tracking-wider font-semibold">
                  Q{qIdx + 1} • {item.topic_id}
                </span>
                <button
                  onClick={() => onSelectTopic(item.topic_id)}
                  className="text-xs text-slate-400 hover:text-sky-300 flex items-center gap-1 transition-colors"
                >
                  <BookOpen size={12} />
                  <span>Topic: <MathText text={item.topic_title} /></span>
                </button>
              </div>

              {/* Question Text */}
              <h3 className="text-base sm:text-lg font-semibold text-white leading-snug mb-4">
                <MathText text={question} />
              </h3>

              {/* Options Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5 mb-4">
                {['a', 'b', 'c', 'd'].map(optKey => {
                  const optText = options[optKey];
                  if (!optText) return null;
                  const isThisSelected = selected === optKey;
                  const isThisCorrect = optKey === correctKey;

                  let btnClass = "mcq-option-btn";
                  if (selected) {
                    if (isThisSelected) {
                      btnClass += isCorrect ? " selected-correct" : " selected-wrong";
                    } else if (isThisCorrect) {
                      btnClass += " show-actual-correct";
                    }
                  }

                  return (
                    <button
                      key={optKey}
                      onClick={() => handleSelectOption(qId, optKey)}
                      className={btnClass}
                    >
                      <span className="font-mono font-bold uppercase w-6 h-6 rounded-md bg-[#252733] flex items-center justify-center text-xs shrink-0 text-slate-300">
                        {optKey}
                      </span>
                      <span className="flex-1 text-left">
                        <MathText text={optText} />
                      </span>
                      {selected && isThisCorrect && (
                        <CheckCircle2 size={18} className="text-emerald-400 shrink-0 mt-0.5" />
                      )}
                      {selected && isThisSelected && !isCorrect && (
                        <XCircle size={18} className="text-rose-400 shrink-0 mt-0.5" />
                      )}
                    </button>
                  );
                })}
              </div>

              {/* Bottom Actions */}
              <div className="flex items-center justify-between pt-3 border-t border-[#272935] text-xs">
                <button
                  onClick={() => toggleExplanation(qId)}
                  className="text-sky-400 hover:text-sky-300 font-medium flex items-center gap-1.5 py-1"
                >
                  <HelpCircle size={14} />
                  {isRevealed ? 'Hide Explanation' : 'View Correct Answer & Explanation'}
                </button>

                {selected && (
                  <span className={`font-semibold ${isCorrect ? 'text-emerald-400' : 'text-rose-400'}`}>
                    {isCorrect ? '✓ Correct Choice!' : `✗ Incorrect (Correct is Option ${correctKey.toUpperCase()})`}
                  </span>
                )}
              </div>

              {/* Explanation Card */}
              {isRevealed && (
                <div className="mt-3 p-4 bg-[#14151b] border border-[#2d303f] rounded-lg text-xs md:text-sm leading-relaxed text-slate-300 animate-fade-in">
                  <div className="font-bold text-emerald-400 mb-1 flex items-center gap-1.5">
                    <Lightbulb size={15} /> Correct Answer: Option ({correctKey.toUpperCase()})
                  </div>
                  <div>
                    <MathText text={explanation} />
                  </div>
                </div>
              )}
            </div>
          );
        })}

        {filteredList.length === 0 && (
          <div className="p-12 text-center text-slate-500 bg-[#16171f] rounded-xl border border-[#2b2d39]">
            <p>No questions found matching your filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
}
