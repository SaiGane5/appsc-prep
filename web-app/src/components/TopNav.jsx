import React from 'react';
import { 
  Menu, 
  BookOpen, 
  HelpCircle, 
  FileText, 
  BarChart3, 
  Star, 
  Type, 
  Calendar
} from 'lucide-react';

export default function TopNav({
  viewMode,
  setViewMode,
  fontSizeMultiplier,
  setFontSizeMultiplier,
  totalBookmarksCount,
  onToggleSidebar,
  examDate = "24/01/2027"
}) {
  const modes = [
    { id: 'notes', label: 'Notes Reader', icon: BookOpen, badge: '40' },
    { id: 'mcqs', label: 'MCQs', icon: HelpCircle, badge: '200' },
    { id: 'mains', label: 'Mains Bank', icon: FileText, badge: '121' },
    { id: 'dashboard', label: 'Dashboard', icon: BarChart3 }
  ];

  return (
    <header className="h-14 shrink-0 bg-[#16171d] border-b border-[#2d2f3c] px-3 sm:px-4 flex items-center justify-between shadow-md z-30">
      {/* Left: Sidebar Toggle & Branding */}
      <div className="flex items-center gap-2 sm:gap-3">
        <button
          onClick={onToggleSidebar}
          className="p-1.5 sm:p-2 text-slate-300 hover:text-white rounded-lg hover:bg-[#22242e] transition-colors"
          title="Toggle Syllabus Index"
        >
          <Menu size={19} />
        </button>

        <div className="flex items-center gap-2">
          <span className="font-extrabold text-sm sm:text-base tracking-tight text-white whitespace-nowrap">
            APPSC <span className="text-sky-400">Group-1</span>
          </span>
          <span className="badge badge-indigo hidden md:inline-flex text-[10px] py-0.5">
            2026–2027
          </span>
        </div>
      </div>

      {/* Center: Mode Tabs */}
      <nav className="flex items-center gap-1 bg-[#1a1b23] p-1 rounded-xl border border-[#2b2d39]">
        {modes.map(mode => {
          const Icon = mode.icon;
          const isActive = viewMode === mode.id;
          return (
            <button
              key={mode.id}
              onClick={() => setViewMode(mode.id)}
              className={`
                flex items-center gap-1.5 px-2.5 sm:px-3 py-1 sm:py-1.5 rounded-lg text-xs font-semibold transition-all
                ${isActive 
                  ? 'bg-sky-500 text-white shadow-sm' 
                  : 'text-slate-400 hover:text-white hover:bg-[#242632]'}
              `}
            >
              <Icon size={14} className="shrink-0" />
              <span className="hidden sm:inline">{mode.label}</span>
              {mode.badge && (
                <span className={`text-[10px] px-1.5 py-0.2 rounded font-mono hidden md:inline ${
                  isActive ? 'bg-sky-700/60 text-white' : 'bg-[#262835] text-slate-400'
                }`}>
                  {mode.badge}
                </span>
              )}
            </button>
          );
        })}
      </nav>

      {/* Right: Font Controls & Exam Reminder */}
      <div className="flex items-center gap-2">
        {/* Font size control */}
        <div className="hidden lg:flex items-center gap-1 bg-[#1a1b23] border border-[#2b2d39] rounded-lg p-0.5 text-xs text-slate-400">
          <button
            onClick={() => setFontSizeMultiplier(prev => Math.max(0.85, prev - 0.08))}
            className="px-2 py-1 hover:text-white hover:bg-[#262835] rounded transition-colors font-mono"
            title="Decrease font size"
          >
            A-
          </button>
          <span className="px-0.5 text-[11px] text-slate-500">|</span>
          <button
            onClick={() => setFontSizeMultiplier(1)}
            className="px-2 py-1 hover:text-white hover:bg-[#262835] rounded transition-colors font-mono"
            title="Reset font size"
          >
            100%
          </button>
          <span className="px-0.5 text-[11px] text-slate-500">|</span>
          <button
            onClick={() => setFontSizeMultiplier(prev => Math.min(1.35, prev + 0.08))}
            className="px-2 py-1 hover:text-white hover:bg-[#262835] rounded transition-colors font-mono"
            title="Increase font size"
          >
            A+
          </button>
        </div>

        {/* Exam Notification Pill */}
        <div className="hidden xl:flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-[#1f2029] border border-[#303342] text-xs text-slate-300">
          <Calendar size={13} className="text-amber-400" />
          <span>Screening: <strong className="text-white">{examDate}</strong></span>
        </div>
      </div>
    </header>
  );
}
