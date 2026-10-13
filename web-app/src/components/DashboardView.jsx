import React from 'react';
import { 
  CheckCircle2, 
  Circle, 
  Star, 
  BookOpen, 
  Award, 
  TrendingUp, 
  Clock, 
  FileText, 
  HelpCircle,
  ArrowRight,
  Sparkles
} from 'lucide-react';

export default function DashboardView({
  manifest,
  allNotes,
  completedTopics,
  bookmarks,
  onSelectTopic,
  onSwitchMode
}) {
  const totalTopics = allNotes.length;
  const completedCount = Object.values(completedTopics).filter(Boolean).length;
  const completionPercent = Math.round((completedCount / totalTopics) * 100);
  const bookmarkCount = Object.values(bookmarks).filter(Boolean).length;

  const totalWords = allNotes.reduce((acc, n) => acc + (n.word_count || 0), 0);
  const totalReadHours = Math.round((totalWords / 180) / 60);

  // Bookmarked notes
  const bookmarkedNotes = allNotes.filter(n => bookmarks[n.topic_id]);

  return (
    <div className="flex-1 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-fade-in">
      {/* Header */}
      <div className="pb-6 mb-8 border-b border-[#2d2f3c]">
        <span className="badge badge-emerald mb-2">Preparation Analytics</span>
        <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
          Syllabus Mastery & Progress Dashboard
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-1">
          Track syllabus coverage across all 7 subject domains for APPSC Group-1 Services 2026–2027.
        </p>
      </div>

      {/* Top Stat Cards Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div className="bg-[#1b1c24] border border-[#2d2f3c] p-5 rounded-2xl shadow-md">
          <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
            <span>Syllabus Coverage</span>
            <CheckCircle2 size={16} className="text-emerald-400" />
          </div>
          <div className="text-3xl font-extrabold text-white font-mono">{completionPercent}%</div>
          <div className="text-[11px] text-slate-400 mt-1">
            {completedCount} of {totalTopics} topics marked complete
          </div>
          <div className="w-full bg-[#252733] h-1.5 rounded-full mt-3 overflow-hidden">
            <div 
              className="bg-emerald-400 h-full rounded-full transition-all duration-500" 
              style={{ width: `${completionPercent}%` }}
            />
          </div>
        </div>

        <div className="bg-[#1b1c24] border border-[#2d2f3c] p-5 rounded-2xl shadow-md">
          <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
            <span>MCQ Practice Bank</span>
            <HelpCircle size={16} className="text-amber-400" />
          </div>
          <div className="text-3xl font-extrabold text-amber-400 font-mono">200</div>
          <div className="text-[11px] text-slate-400 mt-1">
            Prelims screening questions & keys
          </div>
          <button
            onClick={() => onSwitchMode('mcqs')}
            className="text-[11px] text-sky-400 hover:text-sky-300 font-medium flex items-center gap-1 mt-3"
          >
            Start Practice Quiz <ArrowRight size={12} />
          </button>
        </div>

        <div className="bg-[#1b1c24] border border-[#2d2f3c] p-5 rounded-2xl shadow-md">
          <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
            <span>Mains Question Bank</span>
            <FileText size={16} className="text-sky-400" />
          </div>
          <div className="text-3xl font-extrabold text-sky-400 font-mono">121</div>
          <div className="text-[11px] text-slate-400 mt-1">
            Analytical questions with models
          </div>
          <button
            onClick={() => onSwitchMode('mains')}
            className="text-[11px] text-sky-400 hover:text-sky-300 font-medium flex items-center gap-1 mt-3"
          >
            Explore Mains Bank <ArrowRight size={12} />
          </button>
        </div>

        <div className="bg-[#1b1c24] border border-[#2d2f3c] p-5 rounded-2xl shadow-md">
          <div className="flex items-center justify-between text-slate-400 text-xs mb-2">
            <span>Bookmarked Topics</span>
            <Star size={16} className="text-amber-400" />
          </div>
          <div className="text-3xl font-extrabold text-white font-mono">{bookmarkCount}</div>
          <div className="text-[11px] text-slate-400 mt-1">
            Topics saved for quick revision
          </div>
          <div className="text-[11px] text-slate-500 mt-3 font-mono">
            ~{totalWords.toLocaleString()} curated words
          </div>
        </div>
      </div>

      {/* Subject-Wise Progress Breakdown */}
      <div className="bg-[#181921] border border-[#2b2d39] rounded-2xl p-6 mb-8 shadow-lg">
        <h2 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
          <TrendingUp size={18} className="text-sky-400" />
          Subject-Wise Completion Breakdown
        </h2>

        <div className="space-y-4">
          {manifest?.subjects?.map(subject => {
            const subjectNotes = allNotes.filter(n => n.folder === subject.folder);
            const total = subjectNotes.length;
            const completed = subjectNotes.filter(n => completedTopics[n.topic_id]).length;
            const pct = total > 0 ? Math.round((completed / total) * 100) : 0;

            return (
              <div key={subject.folder} className="bg-[#1f2029] border border-[#2d2f3d] p-4 rounded-xl">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
                  <div>
                    <h3 className="text-sm font-semibold text-white">
                      {subject.folder.replace(/^\d+_/, '').replace(/_/g, ' ')}
                    </h3>
                    <div className="text-xs text-slate-400">{subject.paper}</div>
                  </div>
                  <div className="flex items-center gap-3 shrink-0">
                    <span className="text-xs font-mono font-bold text-slate-300">
                      {completed} / {total} Topics ({pct}%)
                    </span>
                    {subjectNotes.length > 0 && (
                      <button
                        onClick={() => {
                          onSelectTopic(subjectNotes[0].topic_id);
                          onSwitchMode('notes');
                        }}
                        className="px-2.5 py-1 text-xs bg-[#292c3a] hover:bg-[#34384a] text-sky-400 hover:text-white rounded-lg transition-colors"
                      >
                        Read
                      </button>
                    )}
                  </div>
                </div>

                <div className="w-full bg-[#13141a] h-2 rounded-full overflow-hidden">
                  <div 
                    className="bg-gradient-to-r from-sky-500 to-emerald-400 h-full rounded-full transition-all duration-500"
                    style={{ width: `${pct}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Bookmarked Topics Section */}
      {bookmarkedNotes.length > 0 && (
        <div className="bg-[#181921] border border-[#2b2d39] rounded-2xl p-6 shadow-lg">
          <h2 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
            <Star size={18} className="text-amber-400" />
            Your Saved Bookmarks ({bookmarkedNotes.length})
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {bookmarkedNotes.map(note => (
              <div
                key={note.topic_id}
                onClick={() => {
                  onSelectTopic(note.topic_id);
                  onSwitchMode('notes');
                }}
                className="p-3.5 bg-[#1f2029] border border-[#2d2f3d] hover:border-amber-400/40 rounded-xl cursor-pointer transition-all hover:bg-[#252733] flex items-start justify-between gap-3 group"
              >
                <div className="min-w-0">
                  <div className="text-[10px] font-mono text-amber-400 font-semibold uppercase">{note.topic_id}</div>
                  <div className="text-xs font-semibold text-white truncate group-hover:text-amber-300 transition-colors">
                    {note.topic_title}
                  </div>
                  <div className="text-[11px] text-slate-400 truncate mt-0.5">{note.subject_title}</div>
                </div>
                <ArrowRight size={15} className="text-slate-500 group-hover:text-amber-400 shrink-0 mt-1 transition-colors" />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
