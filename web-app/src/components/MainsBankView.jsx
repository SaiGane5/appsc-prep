import React, { useState } from 'react';
import MathText from './MathText';
import { 
  BookOpen, 
  ChevronDown, 
  ChevronUp, 
  Search, 
  Filter
} from 'lucide-react';

export default function MainsBankView({ mainsBank, onSelectTopic }) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedSubject, setSelectedSubject] = useState('ALL');
  const [expandedItems, setExpandedItems] = useState({});

  // Parse questions
  const parseMainsItem = (rawText) => {
    if (!rawText.includes('-> Model Approach:')) {
      return { question: rawText, approach: '' };
    }
    const parts = rawText.split('-> Model Approach:');
    return {
      question: parts[0].trim(),
      approach: parts[1] ? parts[1].trim() : ''
    };
  };

  const parsedList = mainsBank.map((item, idx) => ({
    id: `mains-${idx}`,
    ...item,
    parsed: parseMainsItem(item.raw_text)
  }));

  const subjects = ['ALL', ...new Set(parsedList.map(q => q.subject_title))];

  const filteredList = parsedList.filter(item => {
    const matchesSubject = selectedSubject === 'ALL' || item.subject_title === selectedSubject;
    const matchesSearch = !searchQuery || 
      item.parsed.question.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.parsed.approach.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.topic_title.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesSubject && matchesSearch;
  });

  const toggleExpand = (id) => {
    setExpandedItems(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const expandAll = () => {
    const all = {};
    filteredList.forEach(item => { all[item.id] = true; });
    setExpandedItems(all);
  };

  const collapseAll = () => {
    setExpandedItems({});
  };

  return (
    <div className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="pb-5 mb-7 border-b border-[#303036]">
        <h1 className="text-2xl sm:text-3xl font-bold text-white tracking-tight">
          Mains Analytical Questions
        </h1>
        <p className="text-xs sm:text-sm text-zinc-400 mt-1">
          {parsedList.length} Descriptive questions with structured model answer frameworks and evaluation guidelines.
        </p>
      </div>

      {/* Search and Filters */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 mb-6 bg-[#212125] p-2.5 rounded-lg border border-[#303036]">
        <div className="relative flex-1">
          <Search size={13} className="absolute left-3 top-1/2 -translate-y-1/2 text-zinc-400" />
          <input
            type="text"
            placeholder="Search questions..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-8 pr-3 py-1 bg-[#18181b] border border-[#333338] rounded text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400"
          />
        </div>

        <div className="flex items-center gap-2">
          <select
            value={selectedSubject}
            onChange={(e) => setSelectedSubject(e.target.value)}
            className="bg-[#18181b] border border-[#333338] text-xs text-white rounded px-2.5 py-1 focus:outline-none focus:border-zinc-400"
          >
            {subjects.map((s, idx) => (
              <option key={idx} value={s}>
                {s === 'ALL' ? 'All Subjects' : s}
              </option>
            ))}
          </select>

          <button
            onClick={expandAll}
            className="px-2 py-1 bg-[#28282d] hover:bg-[#323238] text-zinc-300 text-xs rounded transition-colors shrink-0"
          >
            Expand All
          </button>
          <button
            onClick={collapseAll}
            className="px-2 py-1 bg-[#28282d] hover:bg-[#323238] text-zinc-300 text-xs rounded transition-colors shrink-0"
          >
            Collapse All
          </button>
        </div>
      </div>

      {/* Question Counter */}
      <div className="text-xs text-zinc-400 mb-3 flex items-center justify-between">
        <span>Showing {filteredList.length} of {parsedList.length} questions</span>
      </div>

      {/* List of Questions */}
      <div className="space-y-4">
        {filteredList.map((item, index) => {
          const isExpanded = !!expandedItems[item.id];
          const { question, approach } = item.parsed;

          return (
            <div
              key={item.id}
              className="bg-[#222226] border border-[#303036] rounded-lg p-5 hover:border-[#404048] transition-colors"
            >
              <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                <span className="text-[11px] font-mono text-zinc-500">
                  #{index + 1} • {item.topic_id}
                </span>
                <button
                  onClick={() => onSelectTopic(item.topic_id)}
                  className="text-xs text-zinc-400 hover:text-white flex items-center gap-1 transition-colors"
                >
                  <BookOpen size={11} />
                  <span>Topic: <MathText text={item.topic_title} /></span>
                </button>
              </div>

              <h3 className="text-base font-medium text-white leading-snug mb-3">
                <MathText text={question} />
              </h3>

              {approach && (
                <div>
                  <button
                    onClick={() => toggleExpand(item.id)}
                    className="w-full mt-2 p-2 bg-[#2a2a2f] hover:bg-[#323238] text-zinc-300 rounded text-xs font-medium flex items-center justify-between transition-colors"
                  >
                    <span>{isExpanded ? 'Hide Model Approach' : 'View Model Answer Approach'}</span>
                    <span className="text-zinc-400">{isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}</span>
                  </button>

                  {isExpanded && (
                    <div className="mt-3 p-3.5 bg-[#1a1a1d] border border-[#333338] rounded text-xs sm:text-sm leading-relaxed text-zinc-300">
                      <div className="font-semibold text-white mb-1.5 text-xs uppercase tracking-wide">
                        Approach:
                      </div>
                      <div className="whitespace-pre-line text-zinc-300">
                        <MathText text={approach} />
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}

        {filteredList.length === 0 && (
          <div className="p-12 text-center text-zinc-500 bg-[#212125] rounded-lg border border-[#303036]">
            <p>No Mains questions found matching your filter criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
}
