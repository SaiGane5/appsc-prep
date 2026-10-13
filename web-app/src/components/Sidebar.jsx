import React, { useState } from 'react';
import MathText from './MathText';
import { 
  CheckCircle, 
  Circle, 
  ChevronRight, 
  ChevronDown, 
  Search, 
  X, 
  Star
} from 'lucide-react';

export default function Sidebar({
  manifest,
  allNotes,
  activeTopicId,
  onSelectTopic,
  completedTopics,
  onToggleComplete,
  bookmarks,
  onToggleBookmark,
  isOpen,
  onClose,
  searchQuery,
  setSearchQuery,
  paperFilter,
  setPaperFilter
}) {
  const [openSubjects, setOpenSubjects] = useState(() => {
    const init = {};
    manifest?.subjects?.forEach(s => { init[s.folder] = true; });
    return init;
  });

  const toggleSubject = (folder) => {
    setOpenSubjects(prev => ({ ...prev, [folder]: !prev[folder] }));
  };

  const filteredNotes = allNotes.filter(note => {
    const matchesSearch = !searchQuery || 
      note.topic_title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      note.syllabus_mapping.toLowerCase().includes(searchQuery.toLowerCase()) ||
      note.subject_title.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesPaper = !paperFilter || paperFilter === 'ALL' ||
      (note.paper && note.paper.toLowerCase().includes(paperFilter.toLowerCase()));

    return matchesSearch && matchesPaper;
  });

  const papers = [
    { id: 'ALL', label: 'All' },
    { id: 'Paper-II', label: 'Paper II' },
    { id: 'Paper-III', label: 'Paper III' },
    { id: 'Paper-IV', label: 'Paper IV' },
    { id: 'Paper-V', label: 'Paper V' },
    { id: 'Screening', label: 'Screening' }
  ];

  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/70 z-40 lg:hidden backdrop-blur-sm transition-opacity"
          onClick={onClose}
        />
      )}

      {/* Sidebar Container */}
      <aside className={`
        fixed inset-y-0 left-0 z-40 w-80 bg-[#18181b] border-r border-[#2d2d33] flex flex-col transition-all duration-200 ease-in-out
        ${isOpen 
          ? 'translate-x-0 lg:static lg:h-full lg:shrink-0 lg:w-80 shadow-xl lg:shadow-none' 
          : '-translate-x-full lg:w-0 lg:hidden lg:overflow-hidden lg:border-none pointer-events-none'}
      `}>
        {/* Header */}
        <div className="p-3.5 border-b border-[#2d2d33] bg-[#1e1e22] shrink-0">
          <div className="flex items-center justify-between mb-2.5">
            <div>
              <h2 className="text-xs font-semibold text-white tracking-wide uppercase">Syllabus Index</h2>
              <div className="text-[11px] text-zinc-400">{allNotes.length} Topics Across 8 Subjects</div>
            </div>
            <button 
              onClick={onClose}
              className="p-1 text-zinc-400 hover:text-white rounded hover:bg-[#28282e] transition-colors"
              title="Close Sidebar"
            >
              <X size={16} />
            </button>
          </div>

          {/* Search Box */}
          <div className="relative mb-2">
            <Search size={13} className="absolute left-2.5 top-1/2 -translate-y-1/2 text-zinc-400" />
            <input 
              type="text"
              placeholder="Search topics..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-8 pr-7 py-1.5 bg-[#141416] border border-[#303036] rounded-md text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-zinc-400 transition-colors"
            />
            {searchQuery && (
              <button 
                onClick={() => setSearchQuery('')}
                className="absolute right-2 top-1/2 -translate-y-1/2 text-zinc-400 hover:text-white"
              >
                <X size={12} />
              </button>
            )}
          </div>

          {/* Paper Filter Tabs */}
          <div className="flex items-center gap-1 overflow-x-auto pb-0.5 no-scrollbar text-[11px]">
            {papers.map(p => (
              <button
                key={p.id}
                onClick={() => setPaperFilter(p.id)}
                className={`px-2 py-0.5 rounded text-[11px] shrink-0 transition-colors ${
                  paperFilter === p.id 
                    ? 'bg-zinc-200 text-zinc-900 font-semibold' 
                    : 'bg-[#25252a] text-zinc-400 hover:text-white hover:bg-[#2d2d33]'
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>

        {/* Subjects & Topics Tree */}
        <div className="flex-1 overflow-y-auto p-2 space-y-2">
          {manifest?.subjects?.map((subject) => {
            const subjectNotes = filteredNotes.filter(n => n.folder === subject.folder);
            if (subjectNotes.length === 0 && (searchQuery || paperFilter !== 'ALL')) {
              return null;
            }

            const totalInSubject = subject.topics.length;
            const completedInSubject = subject.topics.filter(t => {
              const matchedNote = allNotes.find(n => n.folder === subject.folder && n.file_name === t.file);
              return matchedNote && completedTopics[matchedNote.topic_id];
            }).length;

            const isExpanded = openSubjects[subject.folder] ?? true;

            return (
              <div key={subject.folder} className="bg-[#202024] border border-[#2d2d33] rounded-lg overflow-hidden">
                <button
                  onClick={() => toggleSubject(subject.folder)}
                  className="w-full px-3 py-2 flex items-center justify-between text-left hover:bg-[#26262b] transition-colors"
                >
                  <div className="flex items-center gap-1.5 min-w-0 pr-1">
                    <span className="text-zinc-400">
                      {isExpanded ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
                    </span>
                    <span className="text-xs font-medium text-white truncate">
                      {subject.folder.replace(/^\d+_/, '').replace(/_/g, ' ')}
                    </span>
                  </div>
                  <span className="text-[10px] font-mono text-zinc-400 px-1.5 py-0.5 rounded bg-[#161619] shrink-0 border border-[#2b2b30]">
                    {completedInSubject}/{totalInSubject}
                  </span>
                </button>

                {isExpanded && (
                  <div className="p-1 space-y-0.5 border-t border-[#26262a] bg-[#1a1a1d]">
                    {subject.topics.map((topicItem) => {
                      const note = allNotes.find(n => n.folder === subject.folder && n.file_name === topicItem.file);
                      if (!note) return null;
                      
                      const isVisible = filteredNotes.some(fn => fn.topic_id === note.topic_id);
                      if (!isVisible) return null;

                      const isActive = note.topic_id === activeTopicId;
                      const isCompleted = !!completedTopics[note.topic_id];
                      const isBookmarked = !!bookmarks[note.topic_id];

                      return (
                        <div
                          key={note.topic_id}
                          className={`
                            group flex items-center justify-between px-2.5 py-1.5 rounded text-xs cursor-pointer transition-colors
                            ${isActive 
                              ? 'bg-[#2d2d33] text-white font-medium border border-[#44444c]' 
                              : 'text-zinc-300 hover:bg-[#242428] hover:text-white border border-transparent'}
                          `}
                          onClick={() => {
                            onSelectTopic(note.topic_id);
                            if (window.innerWidth < 1024) onClose();
                          }}
                        >
                          <div className="flex items-start gap-2 min-w-0 pr-1">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                onToggleComplete(note.topic_id);
                              }}
                              className="mt-0.5 text-zinc-500 hover:text-zinc-200 transition-colors shrink-0"
                              title={isCompleted ? 'Mark Incomplete' : 'Mark Completed'}
                            >
                              {isCompleted ? (
                                <CheckCircle size={13} className="text-zinc-300 fill-zinc-300/20" />
                              ) : (
                                <Circle size={13} />
                              )}
                            </button>
                            <span className="truncate leading-snug">
                              <MathText text={note.topic_title} />
                            </span>
                          </div>

                          <div className="flex items-center gap-1 shrink-0 ml-1">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                onToggleBookmark(note.topic_id);
                              }}
                              className={`p-0.5 rounded transition-colors ${
                                isBookmarked 
                                  ? 'text-zinc-200' 
                                  : 'text-zinc-600 hover:text-zinc-400 opacity-0 group-hover:opacity-100'
                              }`}
                              title={isBookmarked ? 'Remove Bookmark' : 'Bookmark Topic'}
                            >
                              <Star size={12} fill={isBookmarked ? 'currentColor' : 'none'} />
                            </button>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </aside>
    </>
  );
}
